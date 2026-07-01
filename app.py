import streamlit as st
import pandas as pd
from theme import apply_theme

st.set_page_config(
    page_title="Medical Insurance Cost Prediction",
    page_icon="🏥",
    layout="wide"
)

apply_theme()

df = pd.read_csv("insurance.csv")

st.title("🏥 Medical Insurance Cost Prediction")

st.markdown("""
<div class="card">
This project builds an interactive machine learning app to predict individual medical insurance costs.
The goal is to help insurance companies and users understand which demographic and lifestyle factors
drive healthcare expenses.
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="small-card">
        <div class="metric-number">{df.shape[0]}</div>
        <div class="metric-label">Rows</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="small-card">
        <div class="metric-number">{df.shape[1]}</div>
        <div class="metric-label">Columns</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="small-card">
        <div class="metric-number">${df["charges"].mean():,.0f}</div>
        <div class="metric-label">Average Charge</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="small-card">
        <div class="metric-number">2</div>
        <div class="metric-label">Prediction Models</div>
    </div>
    """, unsafe_allow_html=True)

st.header("Business Case")

st.markdown("""
<div class="card">
Medical insurance companies need to estimate healthcare costs accurately. 
By predicting insurance charges, companies can better understand customer risk,
set fair prices, and identify the most important cost-driving factors.
</div>
""", unsafe_allow_html=True)

st.header("Dataset Introduction")

st.markdown("""
<div class="card">
The dataset contains individual information including age, sex, BMI, number of children,
smoking status, region, and medical insurance charges. The target variable is 
<strong>charges</strong>, which represents the medical insurance cost.
</div>
""", unsafe_allow_html=True)

st.header("Data Preview")
st.dataframe(df.head(), use_container_width=True)

st.header("Project Workflow")

st.markdown("""
<div class="card">
1. Explore the dataset using interactive visualizations.<br>
2. Build two prediction models: Linear Regression and Random Forest.<br>
3. Tune model hyperparameters and compare model performance.<br>
4. Explain the most important variables behind the prediction.<br>
5. Summarize business insights and future improvements.
</div>
""", unsafe_allow_html=True)