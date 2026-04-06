import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# load processed dataset
file_path = "results/processed.csv"
df = pd.read_csv(file_path)

print("Processed dataset loaded successfully!")
print("Shape:", df.shape)

# split features and target
X = df.drop("Label", axis=1)
y = df["Label"]

# train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

# create model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# train model
model.fit(X_train, y_train)

# predictions
y_pred = model.predict(X_test)

# evaluation
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# save model
joblib.dump(model,"results/random_forest_model.pkl")
print("Model saved successfully")