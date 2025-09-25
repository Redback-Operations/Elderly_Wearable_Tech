# Dataset – MRI Alzheimer's Classification

This folder contains MRI brain scan images used to train and test the deep learning model for classifying different stages of Alzheimer's disease.

---

## Classes

Each subfolder represents a cognitive health stage:

- **No Impairment** — Healthy individuals
- **Very Mild Impairment** — Early signs of dementia
- **Mild Impairment** — Noticeable cognitive decline
- **Moderate Impairment** — Significant cognitive decline

---

## Usage

- This directory is used by the Convolutional Neural Network (CNN) model in the **Image Processing** module.
- Images are automatically loaded and preprocessed using directory labels.
- The dataset is split into `train/` and `test/` folders to support proper model evaluation.

---

## Requirements

Make sure to:
- Keep folder names exactly as listed (case-sensitive)
- Maintain class balance for reliable performance
- Map folder names to integer labels (0–3) during preprocessing

---

## 📁 Structure

```
Image Dataset/
├── train/
│   ├── No Impairment/
│   ├── Very Mild Impairment/
│   ├── Mild Impairment/
│   └── Moderate Impairment/
├── test/
│   ├── No Impairment/
│   ├── Very Mild Impairment/
│   ├── Mild Impairment/
│   └── Moderate Impairment/
```

---

