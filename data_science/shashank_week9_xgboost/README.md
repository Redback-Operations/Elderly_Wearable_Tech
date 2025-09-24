# Childhood Obesity Classification – Lachesis (Shashank Samyal)

This package contains my individual contribution to the Lachesis Capstone project:
- **Preprocessing + Ethics** (age banding, BMI, sensitive attribute handling)
- **Model training** (Random Forest baseline, XGBoost benchmark)
- **Reproducible outputs** (metrics, confusion matrix, feature importances)
- **Research** (Geospatial tools for public health; ethics/legality audit)

## 📂 Structure
final-upload/
├─ data/ # official + supporting datasets (see privacy note)
├─ notebooks/ # preprocessing + XGBoost training
├─ outputs/ # saved metrics & plots (evidence)
├─ scripts/ # script versions of the pipeline
└─ reports/ # PDFs: model report + geospatial research


## 🛠️ How to run
1) Install deps:
```bash
pip install numpy pandas scikit-learn xgboost matplotlib
Open notebooks:


jupyter notebook notebooks/pre_processing.ipynb
jupyter notebook notebooks/week9_xgboost.ipynb
Data path:

Place Final_combined_dataset.csv into data/ (or update CSV_PATH at the top of the notebook).

📊 Results (Week 9, XGBoost)
Test Accuracy: 0.8585

CV Mean Accuracy: 0.8665 (±0.0073)

Classes: 7, Features: 25
Artifacts in outputs/:
classification_report.csv, confusion_matrix.png, feature_importances_top.png, summary_metrics.csv, label_classes.csv.

🧭 Geospatial Research
See reports/Geospatial_Tools_Research.pdf for a comparison of ArcGIS, GeoPandas, Kepler.gl, and QGIS, with recommendations for Lachesis (analysis vs. visualisation vs. cost/integration).

🔐 Privacy & Ethics
No direct identifiers used.

Age anonymised into bands; BMI derived from height/weight.

See data/legality_ethics_audit_findings.csv and reports/Obesity_Model_Report.pdf.

👤 Author
Shashank Samyal — ML pipeline & ethics preprocessing (Distinction level submission).


