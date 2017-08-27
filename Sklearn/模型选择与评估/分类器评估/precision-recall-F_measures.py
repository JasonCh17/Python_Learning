#精确率Precision(查准率)

#召回率Recall(查全率)
#F1_Score
#多类多标签分类--Classification Report
from sklearn.metrics import classification_report
y_true=[0,1,2,2,0]
y_pred=[0,0,2,1,0]
target_names=["class 0","class 1","class 2"]
print(classification_report(y_true,y_pred,target_names=target_names))

