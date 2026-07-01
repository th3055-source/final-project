import streamlit as st
from theme import apply_theme

apply_theme()

st.title("✅ Conclusion")

st.markdown("""
<div class="card">
This project developed an interactive machine learning application to predict medical insurance costs.
The app combines data visualization, prediction, hyperparameter tuning, and Explainable AI.
</div>
""", unsafe_allow_html=True)

st.divider()

st.header("Key Findings")

st.markdown("""
<div class="card">
<ul>
<li><strong>Smoking status</strong> is the strongest factor affecting insurance charges.</li>
<li><strong>BMI</strong> and <strong>age</strong> are also important predictors.</li>
<li><strong>Random Forest</strong> performs better than Linear Regression because it captures nonlinear patterns.</li>
<li><strong>Hyperparameter tuning</strong> improves model performance by finding better model settings.</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.header("Business Impact")

st.markdown("""
<div class="card">
This app can help insurance companies estimate medical costs, understand customer risk,
and identify the most important factors behind healthcare expenses. It can also help users
understand why their predicted insurance cost may be high or low.
</div>
""", unsafe_allow_html=True)

st.header("Future Improvements")

st.markdown("""
<div class="card">
<ul>
<li>Use a larger and more diverse dataset.</li>
<li>Test additional models such as XGBoost or Gradient Boosting.</li>
<li>Add SHAP values for more advanced Explainable AI.</li>
<li>Deploy the app with a more detailed user interface for business users.</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.divider()

st.success("Final takeaway: Smoking status, BMI, and age are the main drivers of medical insurance costs, and Random Forest is the best-performing model in this project.")