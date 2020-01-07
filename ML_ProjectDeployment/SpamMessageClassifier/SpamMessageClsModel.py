# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 21:27:50 2020

@author: ssak3
"""

import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pickle

data = pd.read_csv('spam.csv', encoding='latin-1')

dict = {'ham': 0, 'spam': 1}
data['v1'] = data['v1'].map(dict)

data.rename(columns = {'v1':'label', 'v2':'message'}, inplace=True)
data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)

X = data['message']
y = data['label']

cv_X = CountVectorizer()
X = cv_X.fit_transform(X)
pickle.dump(cv_X, open('transform.pkl', 'wb'))

X_train, X_test, y_train, y_test = train_test_split(X, y)

nb_cls = MultinomialNB()
nb_cls.fit(X_train, y_train)

pickle.dump(nb_cls, open('SpamMessageClsModel.pkl', 'wb'))
model = pickle.load(open('SpamMessageClsModel.pkl', 'rb'))

pred = model.predict(X_test)
print(pred)

cm = confusion_matrix(y_test, pred)
acc = ((cm[0,0] + cm[1,1]) / len(y_test)) * 100
print(acc)
