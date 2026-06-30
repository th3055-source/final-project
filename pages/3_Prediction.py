import streamlit as st
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

st.set_page_config(
    page_title="Prediction",
    page_icon="💰",
    layout="wide"
)

df = pd.read_csv("insurance.csv")
df_encoded = pd.get_dummies(df, drop_first=True)

X = df_encoded.drop("charges", axis=1)
y = df_encoded["charges"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
rf_model.fit(X_train, y_train)

lr_r2 = r2_score(y_test, lr_model.predict(X_test))
rf_r2 = r2_score(y_test, rf_model.predict(X_test))

st.title("💰 Insurance Cost Prediction")

st.write("""
This page allows users to estimate medical insurance cost by selecting one of two models.
""")

model_choice = st.radio(
    "Choose a prediction model",
    ["Linear Regression", "Random Forest"]
)

st.divider()

st.subheader("User Input")

age = st.slider("Age", 18, 64, 30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.slider("BMI", 15.0, 55.0, 25.0)
children = st.slider("Children", 0, 5, 0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

input_df = pd.DataFrame({
    "age": [age],
    "bmi": [bmi],
    "children": [children],
    "sex_male": [1 if sex == "male" else 0],
    "smoker_yes": [1 if smoker == "yes" else 0],
    "region_northwest": [1 if region == "northwest" else 0],
    "region_southeast": [1 if region == "southeast" else 0],
    "region_southwest": [1 if region == "southwest" else 0]
})

st.divider()

if model_choice == "Linear Regression":
    prediction = lr_model.predict(input_df)[0]
    model_r2 = lr_r2
else:
    prediction = rf_model.predict(input_df)[0]
    model_r2 = rf_r2

st.header("Prediction Result")

col1, col2 = st.columns(2)

with col1:
    st.metric("Selected Model", model_choice)

with col2:
    st.metric("Model R² Score", f"{model_r2:.3f}")

st.success(f"Predicted Insurance Cost: ${prediction:,.2f}")

st.info("""
Linear Regression is simple and easy to interpret.

Random Forest can capture more complex relationships between variables and usually performs better for this dataset.
""")