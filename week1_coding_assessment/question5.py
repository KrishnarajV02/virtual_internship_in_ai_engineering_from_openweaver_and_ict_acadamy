"""  In the Breast Cancer Prediction kandi 1-click kit, change the algorithm from Support Vector to Decision Trees and showcase the classification metrics along with accuracy, precision and recall displayed separately as well."""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics

cancer  = datasets.load_breast_cancer()
x_train,x_test,y_train,y_test=train_test_split(cancer.data,cancer.target,test_size=0.3,random_state=109)
model = tree.DecisionTreeClassifier()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print("ACCURACY  : ",metrics.accuracy_score(y_test,y_pred))
print("PRECISION : ",metrics.precision_score(y_test,y_pred))
print("RECALL    : ",metrics.recall_score(y_test,y_pred))
