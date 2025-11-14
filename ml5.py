import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

df = pd.read_csv("diabetes.csv")   # load data
print(df.head())

X = df.drop("Outcome", axis=1)     # features
y = df["Outcome"]                  # target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # split

scaler = StandardScaler()          # scaling
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)   # model
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)               # prediction

cm = confusion_matrix(y_test, y_pred)      # evaluation
accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Confusion Matrix:\n", cm)
print("Accuracy:", round(accuracy, 4))
print("Error Rate:", round(error_rate, 4))
print("Precision:", round(precision, 4))
print("Recall:", round(recall, 4))
