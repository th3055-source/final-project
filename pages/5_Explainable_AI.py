import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# -------------------------------
# Page Title
# -------------------------------

st.title("🧠 Explainable AI")

st.write("""
This page explains how the machine learning model makes predictions.

Feature importance from the Random Forest model is used as an Explainable AI technique to identify the most influential variables in predicting medical insurance costs.
""")

# -------------------------------
# Load Dataset
# -------------------------------

df = pd.read_csv("insurance.csv")

# One-hot Encoding
df_encoded = pd.get_dummies(df, drop_first=True)

# Features & Target
X = df_encoded.drop("charges", axis=1)
y = df_encoded["charges"]

# -------------------------------
# Train Random Forest Model
# -------------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# -------------------------------
# Feature Importance
# -------------------------------

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

# -------------------------------
# Plot
# -------------------------------

st.subheader("Explainable AI - Feature Importance")

fig, ax = plt.subplots(figsize=(9,5))

ax.barh(
    importance["Feature"],
    importance["Importance"]
)

ax.invert_yaxis()

plt.xlabel("Importance Score")
plt.ylabel("Features")

st.pyplot(fig)

# -------------------------------
# Top Features
# -------------------------------

st.subheader("Top 3 Most Important Features")

st.table(importance.head(3))

# -------------------------------
# Explanation
# -------------------------------

st.subheader("Model Interpretation")

st.info("""
Explainable AI helps us understand why the machine learning model makes a prediction.

According to the Random Forest model, **smoking status** is the most influential feature affecting medical insurance costs.

**Age** and **BMI** are also highly important because older individuals and people with higher BMI generally require more healthcare services and therefore tend to have higher insurance expenses.

These insights improve the transparency of the prediction model and help users better understand the factors driving medical insurance costs.
""")