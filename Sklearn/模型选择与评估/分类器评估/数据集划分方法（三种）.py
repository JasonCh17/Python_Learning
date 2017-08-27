#K折交叉验证法
#KFold
import numpy as np
from sklearn.model_selection import KFold
X=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
y=np.array([1,2,3,4,5,6])
kf=KFold(n_splits=2)
kf.get_n_splits(X)
print(kf)

for train_index,test_index in kf.split(X):
	print("Train Index:",train_index,",Test Index:",test_index)
	X_train,X_test=X[train_index],X[test_index]
	y_train,y_test=y[train_index],y[test_index]
	# print(X_train,X_test,y_train,y_test)
	
#GroupKFold
import numpy as np
from sklearn.model_selection import GroupKFold
X=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
y=np.array([1,2,3,4,5,6])
groups=np.array([1,2,3,4,5,6])
group_kfold=GroupKFold(n_splits=2)
group_kfold.get_n_splits(X,y,groups)
print(group_kfold)

for train_index,test_index in group_kfold.split(X,y,groups):
	print("Train Index:",train_index,",Test Index:",test_index)
	X_train,X_test=X[train_index],X[test_index]
	y_train,y_test=y[train_index],y[test_index]
	# print(X_train,X_test,y_train,y_test)

#StratifiedKFold
import numpy as np
from sklearn.model_selection import StratifiedKFold
X=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
y=np.array([1,1,1,2,2,2])
skf=StratifiedKFold(n_splits=3)
# skf.get_n_splits(X,y)
print(skf)
# print(skf.get_n_splits(X,y))
for train_index,test_index in skf.split(X,y):
	print("Train Index:",train_index,",Test Index:",test_index)
	X_train,X_test=X[train_index],X[test_index]
	y_train,y_test=y[train_index],y[test_index]
	# print(X_train,X_test,y_train,y_test)


#留一法
#LeaveOneOut
import numpy as np
from sklearn.model_selection import LeaveOneOut
X=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
y=np.array([1,1,1,2,2,2])
loo=LeaveOneOut()
print(loo)
for train_index,test_index in loo.split(X):
	print("Train Index:",train_index,",Test Index:",test_index)
	X_train,X_test=X[train_index],X[test_index]
	y_train,y_test=y[train_index],y[test_index]
	# print(X_train,X_test,y_train,y_test)

#LeavePOut
import numpy as np
from sklearn.model_selection import LeavePOut
X=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
y=np.array([1,1,1,2,2,2])
lpo=LeavePOut(p=2)
print(lpo)
for train_index,test_index in lpo.split(X):
	print("Train Index:",train_index,",Test Index:",test_index)
	X_train,X_test=X[train_index],X[test_index]
	y_train,y_test=y[train_index],y[test_index]
	# print(X_train,X_test,y_train,y_test)


#随机划分法
#ShuffleSplit
import numpy as np
from sklearn.model_selection import ShuffleSplit
X=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
y=np.array([1,2,1,2,1,2])
rs=ShuffleSplit(n_splits=3,test_size=.25,random_state=0)
print(rs)
for train_index,test_index in rs.split(X):
	print("Train Index:",train_index,",Test Index:",test_index)
	X_train,X_test=X[train_index],X[test_index]
	y_train,y_test=y[train_index],y[test_index]
	# print(X_train,X_test,y_train,y_test)
print('============================================================')
rs=ShuffleSplit(n_splits=3,train_size=0.5,test_size=.25,random_state=0)
print(rs)
for train_index,test_index in rs.split(X):
	print("Train Index:",train_index,",Test Index:",test_index)
	X_train,X_test=X[train_index],X[test_index]
	y_train,y_test=y[train_index],y[test_index]
	# print(X_train,X_test,y_train,y_test)

#StratifiedShuffleSplit(优秀)
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
X=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
y=np.array([1,2,1,2,1,2])
sss=StratifiedShuffleSplit(n_splits=3,test_size=.5,random_state=0)
print(sss)
for train_index,test_index in sss.split(X,y):
	print("Train Index:",train_index,",Test Index:",test_index)
	X_train,X_test=X[train_index],X[test_index]
	y_train,y_test=y[train_index],y[test_index]
	# print(X_train,X_test,y_train,y_test)