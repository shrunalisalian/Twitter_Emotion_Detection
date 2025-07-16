import numpy as np 
import pandas as pd
import pickle 

from sklearn.ensemble import GradientBoostingClassifier

# fetch data from data/processed
train_data = pd.read_csv('./data/features/train_bow.csv')

X_train = train_data.iloc[:, 0: -1].values
y_train = train_data.iloc[:, -1].values

# Define and train the model
clf = GradientBoostingClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# save 
pickle.dump(clf, open('model.pkl', 'wb'))