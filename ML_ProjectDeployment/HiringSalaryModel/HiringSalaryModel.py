import pandas as pd
from word2number import w2n
import pickle

data = pd.read_csv("HiringSalary.csv")

data.fillna(0, inplace=True)

data['experience'] = data['experience'].astype(str)
data['experience'] = data['experience'].apply(lambda x: w2n.word_to_num(x))

X = data.iloc[:, [0,1,2]].values
y = data.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
s_LinearRegression = LinearRegression()
s_LinearRegression.fit(X_train, y_train)

# Save the model
pickle.dump(s_LinearRegression, open('HiringSalaryModel.pkl', 'wb'))

# Loading the model to predict the result
model = pickle.load(open('HiringSalaryModel.pkl', 'rb'))
print(model.predict([[20, 10, 10]]))