# #1.通过交叉验证计算得分
# #绘制SVM在digits数据集上的交叉验证曲线
# import numpy as np 
# from sklearn.model_selection import cross_val_score
# from sklearn import datasets,svm 
# digits=datasets.load_digits()
# X=digits.data
# y=digits.target
# svc=svm.SVC(kernel='linear')
# C_s=np.logspace(-10,0,10) #linspace()创建等差数列；logspace()创建等比数列
# print("参数列表长度",len(C_s))
# scores=list()
# scores_std=list()
# for C in C_s:
# 	svc.C=C 
# 	this_scores=cross_val_score(svc,X,y,n_jobs=1)
# 	scores.append(np.mean(this_scores))
# 	scores_std.append(np.std(this_scores))
# #绘制交叉验证曲线
# import matplotlib.pyplot as plt 
# plt.figure(1,figsize=(4,3))
# # plt.clf() #循环绘制
# plt.semilogx(C_s,scores)
# plt.semilogx(C_s,np.array(scores)+np.array(scores_std),'b--')
# plt.semilogx(C_s,np.array(scores)-np.array(scores_std),'b--')
# # locs,labels=plt.yticks()
# # plt.yticks(locs,list(map(lambda x:"%g" % x, locs)))
# plt.ylabel('CV score')
# plt.xlabel('Parameter C')
# plt.ylim(0,1.1)
# plt.show()



# #2.对每个输入数据点产生交叉验证估计(忽略)
# from sklearn import datasets,linear_model
# from sklearn.model_selection import cross_val_score
# diabetes=datasets.load_diabetes()
# X=diabetes.data[:150]
# y=diabetes.target[:150]
# lasso=linear_model.Lasso()
# y_pred=cross_val_score(lasso,X,y)


# #3.计算并绘制模型的学习率曲线
# #绘制学习器的交叉验证学习率曲线
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.naive_bayes import GaussianNB
# from sklearn.svm import SVC
# from sklearn.datasets import load_digits
# from sklearn.model_selection import learning_curve
# from sklearn.model_selection import ShuffleSplit
#
# def plot_learning_curve(estimator,title,X,y,ylim=None,cv=None,n_jobs=1,train_sizes=np.linspace(.1,1,5)):
# 	plt.figure()
# 	plt.title(title)
# 	if ylim is not None:
# 		plt.ylim(*ylim)
# 	plt.xlabel("Training examples")
# 	plt.ylabel("Score")
# 	train_sizes,train_scores,test_scores=learning_curve(
# 		estimator,X,y,cv=cv,n_jobs=n_jobs,train_sizes=train_sizes)
# 	train_scores_mean=np.mean(train_scores,axis=1)
# 	train_scores_std=np.std(train_scores,axis=1)
# 	test_scores_mean=np.mean(test_scores,axis=1)
# 	test_scores_std=np.std(test_scores,axis=1)
# 	plt.grid()
#
# 	plt.fill_between(train_sizes,train_scores_mean-train_scores_std,
# 		train_scores_mean+train_scores_std,alpha=0.1,color='r')
# 	plt.fill_between(train_sizes,test_scores_mean-test_scores_std,
# 		test_scores_mean+test_scores_std,alpha=0.1,color='g')
# 	plt.plot(train_sizes,train_scores_mean,'o-',color='r',label="Training score")
# 	plt.plot(train_sizes,test_scores_mean,'o-',color='g',label="Cross-validation score")
#
# 	plt.legend(loc="best")
# 	return plt
# #套路
# digits=load_digits()
# X,y=digits.data,digits.target
# title="Learning Curve(Naive Bayes)"
# cv=ShuffleSplit(n_splits=100,test_size=.2,random_state=0)
# estimator=GaussianNB()
# plot_learning_curve(estimator,title,X,y,ylim=(0.7,1.01),cv=cv,n_jobs=1)
#
#
# title="Learning Curves (SVM, RBF kernel,$\gamma=0.001$"
# cv=ShuffleSplit(n_splits=10,test_size=.2,random_state=0)
# estimator=SVC(gamma=0.001)
# plot_learning_curve(estimator,title,X,y,ylim=(0.7,1.01),cv=cv,n_jobs=1)
#
# plt.show()
#4.计算并绘制模型的验证曲线(用于参数的选择，绘制不同参数所得的score）
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve
digits=load_digits()
X,y=digits.data,digits.target
param_range=np.logspace(-6,-1,5)
train_scores,test_scores=validation_curve(SVC(),X,y,param_name="gamma",param_range=param_range,cv=10,
										  scoring="accuracy")
train_scores_mean=np.mean(train_scores,axis=1)
train_scores_std=np.std(train_scores,axis=1)
test_scores_mean=np.mean(test_scores,axis=1)
test_scores_std=np.std(test_scores,axis=1)

plt.title("Validation Curve with SVM")
plt.xlabel("$\gamma$")
plt.ylabel("Score")
plt.ylim(0.0,1.1)
lw=2
plt.semilogx(param_range,train_scores_mean,label="Training score",color="darkorange",lw=lw)
plt.fill_between(param_range,train_scores_mean-train_scores_std,
				 train_scores_mean+train_scores_std,alpha=0.2,color="darkorange",lw=lw)

plt.semilogx(param_range,test_scores_mean,label="Cross-validation score",color="navy",lw=lw)
plt.fill_between(param_range,test_scores_mean-test_scores_std,
				 test_scores_mean+test_scores_std,alpha=0.2,color="navy",lw=lw)
plt.legend(loc="best")
plt.show()



#5.通过排序评估交叉验证得分的重要性
