#准确率 Accuracy score
import numpy as np
from sklearn.metrics import accuracy_score
y_pred=[0,2,1,3]
y_true=[0,1,2,3]
a=accuracy_score(y_true,y_pred)
print(a)

b=accuracy_score(y_true,y_pred,normalize=False)
print(b)

#混淆矩阵(错误矩阵)Confusion matrix
from sklearn.metrics import confusion_matrix
y_pred=[2,0,2,2,0,1]
y_true=[0,0,2,2,0,2]
a=confusion_matrix(y_true,y_pred)
print(a)
y_true=["cat","ant","cat","cat","ant","bird"]
y_pred=["ant","ant","cat","cat","ant","cat"]
a=confusion_matrix(y_true,y_pred,labels=["ant","bird","cat"])
print(a)