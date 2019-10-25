# Create Apriori Model for Market Basket Analysis

#Importing pandas library to read CSV data file
import pandas as pd

from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('GroceryStoreDataSet.csv', header = None)
transactions = []
for i in range(0, 22):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 5)])

# Training Apriori on the dataset
rules = apriori(transactions, min_support = 0.5, min_confidence = 0.4, min_lift = 1.2, min_length = 2)

# Create list of results
results = list(rules)

results