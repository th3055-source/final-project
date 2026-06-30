import streamlit as st

st.title("✅ Conclusion")

st.write("""
This project developed a machine learning application to predict medical insurance costs.

The app includes data visualization, prediction using two machine learning models,
hyperparameter tuning, and Explainable AI analysis.
""")

st.subheader("Key Findings")

st.success("""
• Smoking status is the most important factor affecting insurance costs.

• Age and BMI also have significant influence on healthcare expenses.

• Random Forest achieved better prediction performance than Linear Regression.
""")

st.subheader("Business Impact")

st.info("""
Insurance companies can use this application to estimate medical costs,
understand the key cost-driving factors, and support better pricing decisions.
""")

st.subheader("Future Improvements")

st.write("""
- Train with a larger dataset.
- Test additional machine learning models.
- Improve prediction accuracy through more advanced hyperparameter tuning.
- Integrate SHAP values for more detailed Explainable AI.
""")
