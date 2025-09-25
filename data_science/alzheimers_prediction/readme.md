# Alzheimer's Prediction Models

This repository contains two separate deep learning pipelines for Alzheimer's disease prediction:

1. **Text-Based Model** (Previous Semester)
2. **MRI Image-Based Model** (Current Semester)

---

## Repository Structure

```
data_science/
└── alzheimers_prediction/
    ├── Data_processing/       # Code and scripts for text-based prediction
    ├── Image Processing/      # Image model using CNN for MRI classification
```

---

## Project Description

- The **Text-Based Model** was developed in the previous semester to analyze textual health records and predict cognitive decline using NLP and classical ML techniques.

- The **MRI Image-Based Model** is developed in the current semester using a Convolutional Neural Network (CNN) to classify MRI images into cognitive health categories:
  - MildDemented
  - ModerateDemented
  - NonDemented
  - VeryMildDemented

---

## Requirements

- Python 3.8+
- TensorFlow / Keras
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- OpenCV

---

## How to Run

1. Clone this repository.
2. Navigate to either:
   - `Data_processing/` for the text-based model
   - `Image Processing/` for the MRI model
3. Follow the instructions in the respective notebooks to train and evaluate the models.

---
