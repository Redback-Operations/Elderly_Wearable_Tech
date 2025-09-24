import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the dataset
df = pd.read_csv("childhood_obesity.csv")

# 2. Check and clean data
df = df.dropna()

# 3. Define features (X) and target (y)
# Change 'Obesity' to the actual column name for the label in your dataset
X = df.drop("Obesity", axis=1)
y = df["Obesity"]

# 4. Encode categorical features
X = pd.get_dummies(X, drop_first=True)

# 5. Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# 7. Predict
y_pred = model.predict(X_test)

# 8. Metrics
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc*100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 9. Save predictions for sharing
output = X_test.copy()
output["Actual"] = y_test
output["Predicted"] = y_pred
output.to_csv("obesity_predictions.csv", index=False)
print("Predictions saved to obesity_predictions.csv")
