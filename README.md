
# ❤️ Heart Disease Risk Predictor

A simple, interactive web app that estimates a patient's risk of heart disease using a **Gaussian Naive Bayes** classifier, built with **Streamlit**.

## 🔗 Live Demo

**[Try the live app here](https://your-app-name.streamlit.app)** ← replace with your actual Streamlit Cloud URL

## 📌 Overview

This project takes 13 clinical features (age, blood pressure, cholesterol, ECG results, etc.) and predicts whether a patient is likely to have heart disease, along with a confidence score. It's built on the classic **UCI Heart Disease dataset** (303 patient records).

The goal of this project was to go beyond just training a model in a notebook — and turn it into something a non-technical person could actually use and understand.

## 🧠 Model Details

| Detail | Value |
|---|---|
| Algorithm | Gaussian Naive Bayes (`sklearn.naive_bayes.GaussianNB`) |
| Dataset | UCI Heart Disease dataset (303 rows, 13 features) |
| Train/Test Split | 80% / 20% |
| Accuracy | 86.9% |
| Precision | 90.0% |
| Recall | 84.4% |
| F1 Score | 87.1% |

No feature scaling or encoding was applied, as the dataset was already clean and numeric.

## 📋 Features Used

| Feature | Description |
|---|---|
| `age` | Age of the patient (years) |
| `sex` | 1 = male, 0 = female |
| `cp` | Chest pain type (0–3) |
| `trestbps` | Resting blood pressure (mm Hg) |
| `chol` | Serum cholesterol (mg/dL) |
| `fbs` | Fasting blood sugar > 120 mg/dL (1 = true, 0 = false) |
| `restecg` | Resting ECG results (0–2) |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina (1 = yes, 0 = no) |
| `oldpeak` | ST depression induced by exercise relative to rest |
| `slope` | Slope of the peak exercise ST segment (0–2) |
| `ca` | Number of major vessels colored by fluoroscopy (0–4) |
| `thal` | Thalassemia test result (0–3) |

## 🛠️ Tech Stack

- **Python**
- **scikit-learn** — model training
- **pandas** — data handling
- **Streamlit** — interactive web UI
- **Streamlit Community Cloud** — free deployment/hosting

## 📁 Project Structure

```
├── app.py                        # Streamlit app (UI + prediction logic)
├── requirements.txt               # Python dependencies
├── HeartHealthPredictor.pickle    # Trained GaussianNB model
├── HeartHealthPredictor.ipynb     # Notebook: data exploration, training, evaluation
├── heart.csv                      # Dataset
└── README.md
```

## 💻 Run It Locally

```bash
# Clone the repo
git clone https://github.com/Sehrish0508/Heart-Disease-Predictor-model.git
cd Heart-Disease-Predictor-model

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

## ⚠️ Disclaimer

This project is built for **educational purposes only** as part of an AI/ML learning assignment. It is **not** a medical diagnostic tool and should never be used as a substitute for professional medical advice, diagnosis, or treatment.

## 👤 Author

**Sehrish**
Built as part of the Prime AI/ML program.
