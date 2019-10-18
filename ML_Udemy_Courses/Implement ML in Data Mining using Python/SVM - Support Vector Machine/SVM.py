# Create Support Vector Machine (SVM)

#Importing pandas library to read CSV data file
import pandas as pd

#Reading CSV data file in Python
dataset = pd.read_csv('bank_data.csv')

#Dividing dataset into X and y
X = dataset.iloc[:, [0,2,4,5]].values
y = dataset.iloc[:, -1].values

#Importing train_test_split from sklearn.model_selection to split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,  y_test = train_test_split(X,y,test_size=0.2,random_state=0)

#Importing StandardScaler from sklearn.preprocessing to scale matrix of features
from sklearn.preprocessing import StandardScaler
scaled_X = StandardScaler()
X_train = scaled_X.fit_transform(X_train)
X_test = scaled_X.transform(X_test)

#Importing and Fitting SVM to Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)

#Predicting y values using predict method in the class
y_pred = classifier.predict(X_test)

#Creating confusion matrix to find model prediction power
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
