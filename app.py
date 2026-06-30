import streamlit as st
import pandas as pd

# Page setting
st.set_page_config(
    page_title="Medical Insurance Cost Prediction",
    page_icon="🏥",
    layout="wide"
)

# Load data
df = pd.read_csv("insurance.csv")

# Title
st.title("🏥 Medical Insurance Cost Prediction")

st.write("""
This project builds a Streamlit app to predict individual medical insurance costs 
based on demographic and lifestyle factors. The goal is to help users understand 
which factors may increase healthcare expenses.
""")

st.divider()

# Business case
st.header("Business Case")

st.write("""
Medical insurance companies need to estimate healthcare costs accurately. 
By predicting insurance charges, companies can better understand risk, 
set fair prices, and identify the most important cost-driving factors.
""")

# Dataset introduction
st.header("Dataset Introduction")

st.write("""
The dataset contains information about individuals, including age, sex, BMI, 
number of children, smoking status, region, and medical insurance charges.
The target variable is **charges**, which represents the medical insurance cost.
""")

# KPI section
st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Number of Rows", df.shape[0])

with col2:
    st.metric("Number of Columns", df.shape[1])

with col3:
    st.metric("Target Variable", "charges")

# Data preview
st.header("Data Preview")
st.dataframe(df.head())

# Basic statistics
st.header("Basic Statistics")
st.dataframe(df.describe())