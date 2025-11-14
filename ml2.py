import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Load the email spam dataset
df = pd.read_csv('Emails.csv')

# Remove unnecessary columns and separate features & target
X = df.drop(columns=['Prediction', 'Email No.'])   # Features
y = df['Prediction']                               # Target (0 = Not spam, 1 = Spam)

# Split into training and testing data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------------
# K-NEAREST NEIGHBORS CLASSIFIER
# ------------------------------
knn = KNeighborsClassifier(n_neighbors=5)  # Using K=5
knn.fit(X_train, y_train)                  # Train the model
knn_pred = knn.predict(X_test)             # Predict on test data

print("----- KNN -----")
print("Accuracy:", accuracy_score(y_test, knn_pred))                # Accuracy score
print("Confusion Matrix:\n", confusion_matrix(y_test, knn_pred))    # TP/TN/FP/FN table
print("Classification Report:\n", classification_report(y_test, knn_pred))  # Precision, Recall, F1


# ------------------------------
# SUPPORT VECTOR MACHINE CLASSIFIER
# ------------------------------
svm = SVC(kernel='linear')         # Linear kernel works best for text data
svm.fit(X_train, y_train)          # Train SVM model
svm_pred = svm.predict(X_test)     # Predictions

print("----- SVM -----")
print("Accuracy:", accuracy_score(y_test, svm_pred))                # Accuracy
print("Confusion Matrix:\n", confusion_matrix(y_test, svm_pred))    # TP/TN/FP/FN table
print("Classification Report:\n", classification_report(y_test, svm_pred))  # Precision, Recall, F1
