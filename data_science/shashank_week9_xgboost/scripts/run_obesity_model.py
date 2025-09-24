import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

# --- load ---
df = pd.read_csv("obesity.csv")

# --- target & features ---
TARGET = "NObeyesdad"  # e.g., Normal_Weight, Overweight_Level_I, Obesity_Type_I, ...
assert TARGET in df.columns, f"{TARGET} not found. Columns: {list(df.columns)}"

# drop rows with missing values (dataset is usually clean)
df = df.dropna().reset_index(drop=True)

# split X/y
y_text = df[TARGET].astype(str)
X = df.drop(columns=[TARGET])

# identify categorical vs numeric
cat_cols = X.select_dtypes(include=["object"]).columns.tolist()
num_cols = X.select_dtypes(exclude=["object"]).columns.tolist()

# encode target labels (string -> int) for metrics stability
y_le = LabelEncoder()
y = y_le.fit_transform(y_text)

# preprocessors
pre = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
        ("num", "passthrough", num_cols),
    ],
    remainder="drop",
)

# model
clf = RandomForestClassifier(
    n_estimators=400,
    max_depth=None,
    random_state=42,
    n_jobs=-1,
)

pipe = Pipeline(steps=[("prep", pre), ("model", clf)])

# ---- train/valid split (stratified) ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# cross-val accuracy (more credible than single split)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(pipe, X_train, y_train, cv=cv, scoring="accuracy", n_jobs=-1)
print(f"CV Accuracy (mean ± std): {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

# fit and evaluate on held-out test
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {acc:.3f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=y_le.classes_))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# save predictions you can show
out = X_test.copy()
out["Actual"] = y_le.inverse_transform(y_test)
out["Predicted"] = y_le.inverse_transform(y_pred)
out.to_csv("obesity_predictions.csv", index=False)
print("\nSaved predictions -> obesity_predictions.csv")

# small tip on interpretation
topline = (
    f"CV Acc: {cv_scores.mean():.1%} (±{cv_scores.std():.1%}) | "
    f"Test Acc: {acc:.1%} | n_test={len(y_test)}"
)
print("\nSUMMARY:", topline)
