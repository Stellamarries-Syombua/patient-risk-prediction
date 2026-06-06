import streamlit as st

st.set_page_config(
    page_title="Patient Risk Prediction System",
    page_icon="🏥",
    layout="wide"
)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🏥 Patient Risk Prediction System")
st.markdown(
    "End-to-end ML pipeline classifying diabetes patient risk from structured "
    "clinical data — covering EDA, preprocessing, model selection, threshold "
    "tuning, and SHAP explainability."
)

# Key metrics row
col1, col2, col3, col4 = st.columns(4)
col1.metric("ROC-AUC",   "0.821")
col2.metric("Accuracy",  "75.3%")
col3.metric("F1 Score",  "0.627")
col4.metric("Threshold", "0.35")

st.divider()

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Exploratory Analysis",
    "🔧 Preprocessing",
    "🤖 Model Performance",
    "📈 Threshold & CV",
    "🔍 SHAP Explainability",
    "🎯 Risk Segmentation"
])

# ── Tab 1: EDA ────────────────────────────────────────────────────────────────
with tab1:
    st.subheader("Exploratory Data Analysis")

    st.markdown("#### Class Distribution")
    st.image("outputs/figures/plot_01_class_distribution.png", use_column_width=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Feature Distributions")
        st.image("outputs/figures/plot_02_feature_distributions.png", use_column_width=True)
    with c2:
        st.markdown("#### Missing Data Heatmap")
        st.image("outputs/figures/plot_03_missing_heatmap.png", use_column_width=True)

    c3, c4 = st.columns(2)
    with c3:
        st.markdown("#### Correlation with Target")
        st.image("outputs/figures/plot_04_correlation_target.png", use_column_width=True)
    with c4:
        st.markdown("#### Correlation Heatmap")
        st.image("outputs/figures/plot_05_correlation_heatmap.png", use_column_width=True)

    c5, c6 = st.columns(2)
    with c5:
        st.markdown("#### Boxplots by Class")
        st.image("outputs/figures/plot_06_boxplots.png", use_column_width=True)
    with c6:
        st.markdown("#### Pairplot")
        st.image("outputs/figures/plot_07_pairplot.png", use_column_width=True)

# ── Tab 2: Preprocessing ──────────────────────────────────────────────────────
with tab2:
    st.subheader("Data Preprocessing")
    st.markdown("#### Missing Values — Before vs After Imputation")
    st.image("outputs/figures/prep_02_missing_before_after.png", use_column_width=True)
    st.info(
        "Insulin had a 48.7% missing rate — the highest of any feature. "
        "Median imputation was applied within class groups to preserve "
        "the target distribution."
    )

# ── Tab 3: Model Performance ──────────────────────────────────────────────────
with tab3:
    st.subheader("Model Performance")

    st.markdown("#### Metric Comparison Across Models")
    st.image("outputs/figures/plot_09_metric_comparison.png", use_column_width=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### ROC Curves")
        st.image("outputs/figures/plot_10_roc_curves.png", use_column_width=True)
    with c2:
        st.markdown("#### Precision-Recall Curves")
        st.image("outputs/figures/plot_11_pr_curves.png", use_column_width=True)

    st.markdown("#### Confusion Matrices")
    st.image("outputs/figures/plot_12_confusion_matrices.png", use_column_width=True)

    st.markdown("#### Learning Curves")
    st.image("outputs/figures/model_01_learning_curves.png", use_column_width=True)

    st.markdown("#### Error Analysis")
    st.image("outputs/figures/model_02_error_analysis.png", use_column_width=True)

# ── Tab 4: Threshold & CV ─────────────────────────────────────────────────────
with tab4:
    st.subheader("Threshold Tuning & Cross-Validation")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Threshold Analysis")
        st.image("outputs/figures/plot_14_threshold_analysis.png", use_column_width=True)
        st.info(
            "Threshold tuned to **0.35** (down from default 0.50) to "
            "prioritise clinical recall — reducing missed positive cases "
            "at an acceptable precision trade-off."
        )
    with c2:
        st.markdown("#### Cross-Validation ROC-AUC")
        st.image("outputs/figures/plot_13_cv_roc_auc.png", use_column_width=True)

# ── Tab 5: SHAP ───────────────────────────────────────────────────────────────
with tab5:
    st.subheader("SHAP Explainability")
    st.markdown(
        "SHAP (SHapley Additive exPlanations) values show how each feature "
        "pushes a prediction higher or lower — making the model interpretable "
        "for clinical decision-making."
    )

    st.markdown("#### Global Feature Importance")
    st.image("outputs/figures/shap_01_global_importance.png", use_column_width=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Beeswarm Plot")
        st.image("outputs/figures/shap_02_beeswarm.png", use_column_width=True)
    with c2:
        st.markdown("#### Dependence Plots")
        st.image("outputs/figures/shap_03_dependence_plots.png", use_column_width=True)

    st.markdown("#### Individual Patient Explanation — Waterfall (Patient #5)")
    st.image("outputs/figures/shap_04_patient_5_waterfall.png", use_column_width=True)
    st.caption(
        "Glucose is the #1 driver of risk for this patient. "
        "The waterfall chart shows exactly how each feature contributed "
        "to pushing the prediction above the 0.35 threshold."
    )

# ── Tab 6: Risk Segmentation ──────────────────────────────────────────────────
with tab6:
    st.subheader("Risk Tier Segmentation")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Risk Score Distribution")
        st.image("outputs/figures/risk_01_score_distribution.png", use_column_width=True)
    with c2:
        st.markdown("#### Risk Tier Segmentation")
        st.image("outputs/figures/risk_02_tier_segmentation.png", use_column_width=True)

    st.info(
        "Patients are segmented into **Low / Medium / High** risk tiers "
        "based on predicted probability scores, enabling prioritised "
        "clinical follow-up."
    )

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption(
    "Built by Stellamaries Syombua · "
    "Data: Pima Indians Diabetes Dataset · "
    "Model: Gradient Boosting · AUC: 0.821"
)
