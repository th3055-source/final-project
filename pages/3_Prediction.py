import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from theme import apply_theme

apply_theme()

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
    max_depth=5,
    random_state=42
)
rf_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)
rf_pred = rf_model.predict(X_test)

lr_r2 = r2_score(y_test, lr_pred)
rf_r2 = r2_score(y_test, rf_pred)

lr_mse = mean_squared_error(y_test, lr_pred)
rf_mse = mean_squared_error(y_test, rf_pred)

st.title("🤖 Insurance Cost Prediction")

st.markdown("""
<div class="card">
This page allows users to predict medical insurance costs using two machine learning models:
<strong>Linear Regression</strong> and <strong>Random Forest</strong>.
</div>
""", unsafe_allow_html=True)

st.divider()

st.header("Model Selection")

model_choice = st.radio(
    "Choose a prediction model",
    ["Linear Regression", "Random Forest"],
    horizontal=True
)

if model_choice == "Linear Regression":
    selected_model = lr_model
    selected_r2 = lr_r2
    selected_mse = lr_mse
else:
    selected_model = rf_model
    selected_r2 = rf_r2
    selected_mse = rf_mse

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="small-card">
        <div class="metric-number">{selected_r2:.3f}</div>
        <div class="metric-label">R² Score</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="small-card">
        <div class="metric-number">{selected_mse:,.0f}</div>
        <div class="metric-label">MSE</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="small-card">
        <div class="metric-number">{model_choice}</div>
        <div class="metric-label">Selected Model</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.header("User Input")

left_col, right_col = st.columns(2)

with left_col:
    age = st.slider("Age", 18, 64, 30)
    bmi = st.slider("BMI", 15.0, 55.0, 25.0)
    children = st.slider("Number of Children", 0, 5, 0)

with right_col:
    sex = st.selectbox("Sex", ["male", "female"])
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

prediction = selected_model.predict(input_df)[0]

st.divider()

st.header("Prediction Result")

st.markdown(f"""
<div class="card">
<h2 style="color:#0D47A1;">Predicted Insurance Cost: ${prediction:,.2f}</h2>
<p>The prediction is generated using the <strong>{model_choice}</strong> model.</p>
</div>
""", unsafe_allow_html=True)

st.header("Model Comparison")

comparison = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "R² Score": [lr_r2, rf_r2],
    "MSE": [lr_mse, rf_mse]
})

fig = px.bar(
    comparison,
    x="Model",
    y="R² Score",
    title="Model R² Score Comparison",
    labels={"R² Score": "R² Score"}
)
fig.update_layout(height=450, plot_bgcolor="white", paper_bgcolor="white")
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div class="card">
💡 <strong>Model Insight:</strong>
Linear Regression is simple and easy to interpret, while Random Forest can capture more complex relationships.
In this dataset, Random Forest usually performs better because medical insurance cost is affected by nonlinear patterns.
</div>
""", unsafe_allow_html=True)