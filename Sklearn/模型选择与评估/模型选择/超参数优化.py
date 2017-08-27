#网格搜索穷举式超参数优化方法
from sklearn import svm,datasets
from sklearn.model_selection import GridSearchCV
iris=datasets.load_iris()
#定义网格参数
parameters={'kernel':('rbf','linear'),
'C':[1,5,10]}
svr=svm.SVC()
clf =GridSearchCV(svr,parameters)

# print(clf.get_params().keys())
clf.fit(iris.data,iris.target)
print(clf.best_estimator_)

#随机采样式超参数优化方法
import  numpy as np
from time import time
from scipy.stats import  randint as sp_randint
from sklearn.model_selection import RandomizedSearchCV
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
#用于报告超参数搜索的最好结果的函数
def report(results,n_top=3):
	for i in range(1,n_top + 1):
		candidates=np.flatnonzero(results['rank_test_score']==i)
		for candidate in candidates:
			print("Model with rank:{0}".format(i))
			print("Mean validation score:{0:.3f}±{1:.3f}".format(
				results['mean_test_score'][candidate],
				results['std_test_score'][candidate]))
			print("Parameter:{0}".format(results['params'][candidate]))
			print("")
#读取数据
digits=load_digits()
X,y=digits.data,digits.target
#构建分类器
clf=RandomForestClassifier(n_estimators=20)
#设置想要优化的超参数以及他们的取值分布
param_dist={"max_depth":[3,None],
"max_features":sp_randint(1,11),
"min_samples_split":sp_randint(2,11),
"bootstrap":[True,False],
"criterion":["gini","entropy"]}
#开启超参数空间的随机搜索
n_iter_search=20
random_search=RandomizedSearchCV(clf,param_distributions=param_dist, n_iter=n_iter_search,error_score=0)  #,n_jobs=2
start=time()
random_search.fit(X,y)
print("RandomizedSearchCV took %.2f seconds for %d candidates"
	" parameter settings."% ((time()-start),n_iter_search))
report(random_search.cv_results_)