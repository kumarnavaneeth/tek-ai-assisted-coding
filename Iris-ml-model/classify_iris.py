import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset from the data folder
iris = pd.read_csv("data/Iris.csv")

# Use the four feature columns and species as the label
X = iris[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
y = iris["Species"]

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple decision tree classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model on the test set
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
print("\nClassification report:\n", classification_report(y_test, predictions))

# Example prediction: sample iris measurements
sample = [[5.1, 3.5, 1.4, 0.2]]
print("Example sample prediction:", model.predict(sample)[0])
