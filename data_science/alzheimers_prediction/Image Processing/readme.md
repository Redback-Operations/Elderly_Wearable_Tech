# Alzheimer's MRI Image Classification using CNN

This project implements a deep learning pipeline to classify brain MRI images into four stages of cognitive health, including Alzheimer's disease, using a custom Convolutional Neural Network (CNN).

---

## Problem Statement

Early and accurate detection of Alzheimer's disease is crucial. This project aims to automate the classification of MRI brain images into the following classes:

- **MildDemented**  
- **ModerateDemented**  
- **NonDemented**  
- **VeryMildDemented**

---

## 📁 Repository Structure

```
.
├── Image Dataset/           # Contains structured image folders by class
├── model.ipynb              # Jupyter notebook with preprocessing, training, evaluation
├── readme.md                # Project documentation
```

---

## Dataset

The dataset used is the **Alzheimer's Dataset (4 Class of Images)** available on Kaggle:  
🔗 https://www.kaggle.com/datasets/sachinkumar413/alzheimer-dataset-4-class-of-images

Dataset directory structure:

```
Image Dataset/
└── train/
    ├── MildDemented/
    ├── ModerateDemented/
    ├── NonDemented/
    └── VeryMildDemented/
```

---

## Model Architecture

- 3 Convolutional Layers with ReLU activation  
- MaxPooling after each convolutional layer  
- Dense layer with 1024 neurons  
- Dropout for regularization  
- Final softmax layer for multi-class classification  

**Achieved over 98% accuracy on the test set**

---

## 🔧 Requirements

- Python 3.8+
- TensorFlow 2.x
- OpenCV
- scikit-learn
- imbalanced-learn
- seaborn
- matplotlib
- pandas

### Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Model

1. Place the dataset in the correct directory structure.
2. Open `model.ipynb` in Jupyter Notebook or Google Colab.
3. Run all cells to preprocess the data, train the model, and view evaluation results.

---

## Outputs

- Training vs Validation Accuracy/Loss curves  
- Classification Report (Precision, Recall, F1-Score)  
- Confusion Matrix Heatmap  
- Random image grid with predicted vs actual labels  

---

## Contributors

- **Om** – Lead developer, model implementation, training and evaluation  
- **Aryan** – Dataset structuring and support  

---
