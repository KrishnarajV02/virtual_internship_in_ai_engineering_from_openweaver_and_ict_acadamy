""" Write a python program to showcase the use of confusion_matrix function from sklearn.metrics to compute a confusion matrix for binary classification. Use pandas to label the rows and columns of the confusion matrix for better readability. Upload screenshots of both the code and the output (upload only in PNG image format).
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import pandas as pd

cancer = datasets.load_breast_cancer()

x_train,x_test,y_train,y_test=train_test_split(cancer.data,cancer.target,test_size=0.3,random_state=109)
model = svm.SVC(kernel="linear")
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

colm = ["PPEDICTED "+i.upper() for i in cancer.target_names]
rows = ["ACTUAL "+i.upper() for i in cancer.target_names]
confusion_matrix=pd.DataFrame(metrics.confusion_matrix(y_test,y_pred),columns=colm,index=rows)

confusion_matrix
