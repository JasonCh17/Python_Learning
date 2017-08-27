from sklearn.metrics import roc_curve
import numpy as np
import matplotlib.pyplot as plt
y=np.array([1,1,2,2])
scores=np.array([0.1,0.4,0.35,0.8])
fpr,tpr,threshold=roc_curve(y,scores,pos_label=2)
print(fpr)
print(tpr)
# print(threshold)
# plt.plot(fpr,tpr)
# plt.show()

# from sklearn.metrics import roc_auc_score
# y_true=np.array([0,0,1,1])
# y_scores=np.array([0.1,0.4,0.35,0.8])

# print(roc_auc_score(y_true,y_scores))