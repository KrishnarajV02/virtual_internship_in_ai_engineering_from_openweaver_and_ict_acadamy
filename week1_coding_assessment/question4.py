""" In this week’s kandi 1-click kit on Breast Cancer Prediction, perform hyperparameter tuning to find the optimal values for SVM's hyperparameters (e.g., C and gamma). Use techniques like grid search or random search to explore different combinations of hyperparameters and choose the best performing ones. """


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import GridSearchCV
import numpy as np

cancer = datasets.load_breast_cancer()
model = svm.SVC()
grid_space={"C" : [0.001, 0.01, 0.1, 1, 10, 100],
            "gamma" : [0.001, 0.01, 0.1, 1, 10, 100],
            "random_state":np.arange(105,112,1) 
           }
grid = GridSearchCV(model,param_grid=grid_space,scoring="accuracy")
grid.fit(cancer.data,cancer.target )

print("Best Accuracy Score : ",grid.best_score_)
print("Best Parameters     ; ",grid.best_params_)
