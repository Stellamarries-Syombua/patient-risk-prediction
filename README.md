# 🏥 Patient Risk Prediction System

**An end-to-end Machine Learning pipeline for predicting diabetes risk in patients using clinical data.**

This project demonstrates a complete data science workflow — from exploratory data analysis to model deployment — built with a strong emphasis on **clinical interpretability** and practical utility.

![Streamlit App](https://github.com/Stellamarries-Syombua/patient-risk-prediction/blob/master/outputs/figures/plot_01_class_distribution.png)

## ✨ Live Demo

Try the interactive web app:  
**[🚀 Open Streamlit App](https://patient-risk-prediction.streamlit.app/)** *(if deployed)*

Or run it locally (instructions below).

## 📋 Project Overview

This repository contains a comprehensive analysis of the **Pima Indians Diabetes Database**. The goal is to build a reliable model that can help healthcare professionals identify patients at high risk of diabetes, with transparent explanations for each prediction.

### Key Highlights
- **Dataset**: Pima Indians Diabetes (768 records, 9 features)
- **Best Model**: Gradient Boosting (ROC-AUC: **0.821**)
- **Clinical Threshold**: Optimized at **0.35** (prioritizing recall)
- **Explainability**: Full SHAP analysis for model transparency
- **Deployment**: Streamlit web application

## 🗂️ Repository Structure
patient-risk-prediction/
├── notebooks/                  # Jupyter notebooks (step-by-step workflow)
│   ├── 01 data_loading_overview.ipynb
│   ├── 02 exploratory_data_analysis.ipynb
│   ├── 03 preprocessing_pipeline.ipynb
│   ├── 04 model_building_evaluation.ipynb
│   └── 05 explainability_final_report.ipynb
├── data/
│   └── diabetes.csv            # Raw dataset
├── outputs/
│   ├── figures/                # All generated plots
│   └── patient_risk_prediction_report.txt
├── app.py                      # Streamlit web application
├── requirements.txt
└── README.md
text

## 📊 Dataset

The dataset contains diagnostic measurements for female patients of Pima Indian heritage who are at least 21 years old.

**Features**:
- `Pregnancies` — Number of times pregnant
- `Glucose` — Plasma glucose concentration (2h oral glucose tolerance test)
- `BloodPressure` — Diastolic blood pressure (mmHg)
- `SkinThickness` — Triceps skinfold thickness (mm)
- `Insulin` — 2-hour serum insulin (mu U/ml)
- `BMI` — Body mass index
- `DiabetesPedigreeFunction` — Genetic risk score
- `Age` — Age in years
- `Outcome` — Target (1 = Diabetes, 0 = No Diabetes)

## 🔄 Workflow

1. **Data Loading & Quality Audit**
2. **Exploratory Data Analysis** (visualizations, correlations, outliers)
3. **Preprocessing** (handling zeros as missing, imputation, scaling)
4. **Model Training & Evaluation** (multiple classifiers, cross-validation)
5. **Threshold Optimization** (clinical recall focus)
6. **Explainability** (SHAP values)
7. **Risk Tier Segmentation**
8. **Web Deployment** (Streamlit)

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Stellamarries-Syombua/patient-risk-prediction.git
cd patient-risk-prediction
2. Install dependencies
Bashpip install -r requirements.txt
3. Run the Streamlit app
Bashstreamlit run app.py
📈 Model Performance
MetricScoreROC-AUC0.821Accuracy75.3%F1 Score0.627Precision~0.58Recall~0.68
Note: Threshold lowered to 0.35 to improve detection of at-risk patients.
🔍 Interpretability
The model uses SHAP (SHapley Additive exPlanations) to show exactly how each clinical feature influences individual risk predictions. This is crucial for building trust in healthcare AI applications.
🛠️ Technologies Used

Python — Core language
Pandas / NumPy — Data manipulation
Scikit-learn — Modeling & evaluation
SHAP — Model explainability
Matplotlib / Seaborn — Visualization
Streamlit — Interactive web app

🙋‍♀️ Author
Stellamaries Syombua
Healthcare Data Analyst & Biostatistician
Passionate about using data science to improve patient outcomes.
