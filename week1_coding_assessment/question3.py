"""  Write a Python program utilizes the NumPy library to split the Iris dataset into training and testing sets, and what are the implications of specifying the test_size parameter and the random_state parameter in the context of this train-test split? Additionally, what information is provided by the displayed shapes of the resulting arrays? """

def custom_train_test_split(data,target,test_size,random_state):
    import numpy as np
    np.random.seed(random_state)
    np.random.shuffle(data)
    np.random.seed(random_state)
    np.random.shuffle(target)
    train_size=int((1-test_size)*np.shape(data)[0])
    train_data = data[:train_size]
    test_data = data[train_size:]
    train_target = target[:train_size]
    test_target = target[train_size:]
    return train_data,test_data,train_target,test_target

from sklearn import datasets
iris = datasets.load_iris()
x_train,x_test,y_train,y_test=custom_train_test_split(iris.data,iris.target,test_size=0.3,random_state=109)
print("Training Data Shape   : ",x_train.shape)
print("Testing Data Shape    : ",x_test.shape)
print("Training Target Shape : ",y_train.shape)
print("Testing Target Shape  : ",y_test.shape)
