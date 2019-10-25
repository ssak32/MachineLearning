# Create ANN Model

#Importing pandas library to read CSV data file
import pandas as pd

#Reading CSV data file into Python
dataset = pd.read_csv('Bank_Data.csv')
X = dataset.iloc[:, 0:6].values
y = dataset.iloc[:, 6].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 3] = labelencoder_X_2.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

# Dividing dataset into Training set and Testing set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Scaling Inputs
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Importing Keras libraries
import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

# Adding input layer and first hidden layer
classifier.add(Dense(output_dim = 4, init = 'uniform', activation = 'relu', input_dim = 6))

# Adding second hidden layer
classifier.add(Dense(output_dim = 4, init = 'uniform', activation = 'relu'))

# Adding output layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

# Compiling ANN Algorithm
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting ANN Algorithm to Training set
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 50)

# Predicting y_test using X_test 
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

#Creating Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
