# Alzheimer's Disease Prediction 

This project is an **Alzheimer's Disease Prediction Notebook** using **machine learning models**. It is designed to predict the **onset** or **progression** of Alzheimer's disease by analyzing clinical and neuroimaging data. The notebook performs **data preprocessing**, **feature engineering**, **model training**, **evaluation**, and **visualization** to help diagnose Alzheimer's with high accuracy.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data Structure](#data-structure)
6. [Modeling Process](#modeling-process)
7. [Results](#results)
8. [Future Enhancements](#future-enhancements)
9. [Contributing](#contributing)
10. [License](#license)

---

## Project Overview

The **Alzheimer's Disease Prediction** project uses machine learning models to analyze clinical and neuroimaging data. The goal is to predict the onset or progression of Alzheimer's disease and identify the most important features contributing to the prediction. With a focus on **Random Forest** models and **SMOTE** for handling class imbalance, the project achieves high accuracy in diagnosing Alzheimer's disease.

---

## Features

- **Data Preprocessing**: Clean and normalize the data, handling missing values and scaling features.
- **Exploratory Data Analysis (EDA)**: Visualize key features such as age, CDR (Clinical Dementia Rating), and nWBV (Normalized Whole Brain Volume).
- **Model Building**: Train a **Random Forest classifier**, optimize hyperparameters using **GridSearchCV**, and handle class imbalance using **SMOTE**.
- **Model Evaluation**: Evaluate models using accuracy, precision, recall, F1-score, and confusion matrix.
- **Feature Importance**: Visualize the most important features contributing to Alzheimer's prediction.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Redback-Operations/redback-senior-tech/tree/main/data_science/alzheimers_prediction
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd alzheimers-prediction-dashboard
   ```

3. **Install Required Dependencies**: You need Python 3.x installed along with the following libraries:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn imbalanced-learn
   ```

4. **Run the Notebook**:
   ```bash
   jupyter notebook task.ipynb
   ```

---

## Usage

### Upload Alzheimer's Data:
- The notebook loads a dataset containing clinical and neuroimaging data which can be found within the Data Warehouse.
- Ensure the dataset is correctly formatted and structured as expected for the best results.

### Train and Test the Model:
- The notebook trains a **Random Forest classifier** on the preprocessed data.
- **SMOTE** is used to handle class imbalance, improving prediction performance on underrepresented classes.

### Model Evaluation:
- Evaluate the model based on key metrics: **accuracy**, **precision**, **recall**, **F1 score**, and **feature importance** analysis.

---

## Data Structure

The dataset should contain the following key columns:

- `Subject ID`: Unique identifier for the subject.
- `Age`: Age of the subject.
- `CDR`: Clinical Dementia Rating.
- `nWBV`: Normalized Whole Brain Volume.
- `ASF`: Atlas Scaling Factor.
- `MMSE`: Mini-Mental State Examination score.

Ensure the dataset is clean and contains no missing or erroneous values.

---

## Modeling Process

1. **Data Preprocessing**: 
   - Handle missing values, normalize features, and split the data into training and testing sets.
  
2. **Feature Selection**: 
   - Use **Recursive Feature Elimination (RFE)** to select the most important features for prediction.

3. **Model Building**: 
   - Train various models including **Logistic Regression**, **SVM**, and **Random Forest**, and use **GridSearchCV** for hyperparameter tuning.

4. **Class Imbalance Handling**: 
   - Use **SMOTE** to balance the classes and improve model performance on underrepresented categories.

---

## Results

- **Test Set Accuracy**: The best-performing **Random Forest model** achieved an accuracy of **99.2%** on the test set after applying SMOTE for class balancing.

- **Classification Report (with SMOTE)**:
   ```plaintext
   Precision   Recall   F1-Score  Support
   0:    0.99       0.99      0.99       72
   1:    0.98       0.98      0.98       66
   2:    1.00       1.00      1.00       58
   3:    1.00       1.00      1.00       60
   ```

- **Feature Importance**:
   1. `nWBV (Normalized Whole Brain Volume)` - Importance: **0.2118**
   2. `CDR (Clinical Dementia Rating)` - Importance: **0.1808**
   3. `Age` - Importance: **0.1263**
   4. `ASF (Atlas Scaling Factor)` - Importance: **0.1084**

---

## Future Enhancements

Possible future improvements and features:

- **XGBoost Model**: Try using **XGBoost** for potentially better performance.
- **SHAP Analysis**: Use **SHAP** to provide deeper insights into feature importance.
- **Additional Data**: Incorporate other biomarkers or imaging data for a more comprehensive model.
- **Deployment**: Deploy the model as a web application using **Flask** or **Dash** for real-time predictions.

---

## Contributing

Contributions are welcome! Feel free to open a pull request or submit an issue if you have suggestions or improvements. Please follow the standard GitHub workflow for contributing to the project.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

