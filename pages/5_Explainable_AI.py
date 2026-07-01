import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.ensemble import RandomForestRegressor
from theme import apply_theme

apply_theme()

df = pd.read_csv("insurance.csv")
df_encoded = pd.get_dummies(df, drop_first=True)

X = df_encoded.drop("charges", axis=1)
y = df_encoded["charges"]

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
model.fit(X, y)

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values("Importance", ascending=False)

st.title("🧠 Explainable AI")

st.markdown("""
<div class="card">
This page explains how the Random Forest model makes predictions.
Feature importance is used as an Explainable AI method to identify the most influential variables.
</div>
""", unsafe_allow_html=True)

st.divider()

st.header("Feature Importance Overview")

top_n = st.slider(
    "Select number of features to display",
    min_value=3,
    max_value=len(importance),
    value=6
)

top_features = importance.head(top_n)

fig = px.bar(
    top_features,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Top Feature Importance Scores",
    labels={"Importance": "Importance Score", "Feature": "Feature"}
)
fig.update_layout(
    height=500,
    plot_bgcolor="white",
    paper_bgcolor="white",
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.header("Top Driving Variables")

col1, col2, col3 = st.columns(3)

top1 = importance.iloc[0]
top2 = importance.iloc[1]
top3 = importance.iloc[2]

with col1:
    st.markdown(f"""
    <div class="small-card">
        <div class="metric-number">{top1["Feature"]}</div>
        <div class="metric-label">Most Important Feature</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="small-card">
        <div class="metric-number">{top2["Feature"]}</div>
        <div class="metric-label">Second Feature</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="small-card">
        <div class="metric-number">{top3["Feature"]}</div>
        <div class="metric-label">Third Feature</div>
    </div>
    """, unsafe_allow_html=True)

st.subheader("Feature Importance Table")
st.dataframe(importance, use_container_width=True)

st.divider()

st.header("Model Interpretation")

selected_feature = st.selectbox(
    "Select a feature to view interpretation",
    importance["Feature"].tolist()
)

if selected_feature == "smoker_yes":
    explanation = """
    Smoking status is the strongest driver of insurance cost.
    Smokers usually have higher health risks, which leads to higher expected medical expenses.
    """
elif selected_feature == "bmi":
    explanation = """
    BMI is an important continuous variable.
    Higher BMI can be associated with higher medical risk, especially when combined with smoking.
    """
elif selected_feature == "age":
    explanation = """
    Age is important because older individuals generally require more healthcare services.
    """
else:
    explanation = """
    This feature contributes to the prediction, but its impact is smaller compared with smoking, BMI, and age.
    """

st.markdown(f"""
<div class="card">
💡 <strong>Interpretation for {selected_feature}:</strong><br><br>
{explanation}
</div>
""", unsafe_allow_html=True)

st.header("Explainable AI Takeaway")

st.markdown("""
<div class="card">
Explainable AI helps turn the model from a black box into an understandable decision tool.
For this dataset, the Random Forest model mainly relies on <strong>smoking status</strong>,
<strong>BMI</strong>, and <strong>age</strong> when predicting insurance charges.
</div>
""", unsafe_allow_html=True)