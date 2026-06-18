# Patient Risk Prediction System

**Predicting Diabetes Risk in Patients using Clinical Data and Machine Learning**

---

## Abstract

This project develops and evaluates a machine learning pipeline to predict the risk of diabetes in patients based on clinical and demographic features from the Pima Indians Diabetes Dataset. The study emphasizes model interpretability (using SHAP) to support clinical decision-making. The best-performing model achieved a ROC-AUC of 0.821, with a clinically optimized threshold to maximize early detection of at-risk patients.

## Objectives

- To perform comprehensive exploratory data analysis on patient clinical measurements.
- To build, train, and compare multiple machine learning models for binary diabetes classification.
- To optimize the decision threshold with a focus on clinical recall (minimizing missed high-risk cases).
- To provide model interpretability using SHAP values for transparency and trust in healthcare settings.
- To develop an interactive web application for real-time risk prediction.

## Dataset Description

The analysis uses the **Pima Indians Diabetes Database**, consisting of 768 female patients of Pima Indian heritage (age ≥ 21 years). The dataset includes the following features:

- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration (mg/dL)
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (kg/m²)
- **DiabetesPedigreeFunction**: Diabetes pedigree function (genetic risk score)
- **Age**: Age in years
- **Outcome**: Target variable (0 = No diabetes, 1 = Diabetes)

## Methods

### 1. Data Preprocessing
- Identified and handled zero values as missing data in Glucose, BloodPressure, BMI, SkinThickness, and Insulin.
- Applied median imputation for missing values.
- Feature scaling using StandardScaler.
- Train-test split (80/20) with stratification.

### 2. Exploratory Data Analysis
- Univariate and bivariate analysis
- Correlation matrices
- Distribution plots and boxplots for outlier detection
- Class distribution analysis (imbalanced dataset)

### 3. Model Development
Multiple classification algorithms were evaluated:
- Logistic Regression
- Random Forest
- Gradient Boosting (XGBoost / LightGBM)
- Support Vector Machine
- K-Nearest Neighbors

Models were tuned using cross-validation. Performance was measured using Accuracy, Precision, Recall, F1-score, and ROC-AUC.

### 4. Interpretability Analysis
SHAP (SHapley Additive exPlanations) values were computed to understand feature contributions to individual predictions.

### 5. Deployment
A user-friendly web application was built using **Streamlit** for real-time patient risk assessment.

## 📈 Results & Interpretation

### Model Performance (Best Model: Gradient Boosting)

| Metric          | Value     | Interpretation |
|-----------------|-----------|----------------|
| ROC-AUC         | 0.821     | Good discriminatory ability |
| Accuracy        | 75.3%     | Solid overall performance |
| Recall          | 0.68      | Improved with threshold tuning |
| Precision       | ~0.58     | Moderate |
| F1 Score        | 0.627     | Balanced metric |

**Key Clinical Insight**: Lowering the classification threshold to **0.35** significantly improved recall, allowing better identification of patients who need early intervention.

**Top Predictive Features (based on SHAP analysis)**:
1. **Glucose** : Most influential feature (higher levels strongly increase risk)
2. **BMI**
3. **Age**
4. **DiabetesPedigreeFunction**
5. **Pregnancies**

## 🏁 Conclusions & Recommendations

- The developed model demonstrates strong potential as a clinical decision support tool.
- Glucose level remains the dominant risk factor, consistent with medical literature.
- SHAP-based explanations enhance model trustworthiness for healthcare professionals.
- Future work could include:
  - Integration of additional clinical variables (e.g., HbA1c)
  - External validation on diverse populations
  - Prospective clinical trials

This project highlights how data science can support preventive healthcare while maintaining interpretability and clinical relevance.

## Technologies Used

- **Languages**: Python, Jupyter Notebooks
- **Data Science**: Pandas, NumPy, Scikit-learn, SHAP
- **Visualization**: Matplotlib, Seaborn
- **Deployment**: Streamlit
- **Version Control**: Git & GitHub

## How to Use This Repository

1. Clone the repo:
   ```bash
   git clone https://github.com/Stellamarries-Syombua/patient-risk-prediction.git
