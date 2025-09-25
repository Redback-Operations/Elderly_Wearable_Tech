# MRI Image Dataset for Alzheimer's Classification

This directory contains the MRI brain scan dataset used for the **image-based Alzheimer's prediction model**.

---

## Structure

```
Image Dataset/
├── train/
│   ├── MildDemented/
│   ├── ModerateDemented/
│   ├── NonDemented/
│   └── VeryMildDemented/
├── test/
│   ├── MildDemented/
│   ├── ModerateDemented/
│   ├── NonDemented/
│   └── VeryMildDemented/
```

Each subfolder represents a class of cognitive condition. The model uses these folders to train and evaluate a CNN classifier.

---

## Source

The original dataset can be found here on Kaggle:  
🔗 [Alzheimer's Dataset (4 Class of Images)](https://www.kaggle.com/datasets/sachinkumar413/alzheimer-dataset-4-class-of-images)

---

## Usage

This dataset is used by the CNN model defined in the **Image Processing** module. The notebook:
```
Image Processing/model.ipynb
```
loads this dataset, preprocesses it, and trains the model.

---

## Note

Make sure that:
- Directory names match exactly (case-sensitive)
- Images are correctly labeled for consistent results

---
