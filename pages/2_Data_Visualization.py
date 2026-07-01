import streamlit as st
import pandas as pd
import plotly.express as px
from theme import apply_theme

apply_theme()

df = pd.read_csv("insurance.csv")

st.title("📊 Data Visualization")

st.markdown("""
<div class="card">
This page highlights four key visual patterns in the medical insurance dataset.
Each chart focuses on one important relationship related to insurance charges.
</div>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------
# Graph 1
# -----------------------------
st.header("1. Distribution of Insurance Charges")

fig1 = px.histogram(
    df,
    x="charges",
    nbins=35,
    title="Distribution of Insurance Charges",
    labels={"charges": "Insurance Charges"}
)
fig1.update_layout(height=460, plot_bgcolor="white", paper_bgcolor="white")
st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
<div class="card">
💡 <strong>Insight:</strong> Most insurance charges are concentrated in the lower range,
while a small number of people have very high medical expenses.
</div>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------
# Graph 2
# -----------------------------
st.header("2. Average Charges by Smoking Status")

smoker_avg = df.groupby("smoker")["charges"].mean().reset_index()

fig2 = px.bar(
    smoker_avg,
    x="smoker",
    y="charges",
    title="Average Charges by Smoking Status",
    labels={"smoker": "Smoker", "charges": "Average Charges"}
)
fig2.update_layout(height=460, plot_bgcolor="white", paper_bgcolor="white")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
<div class="card">
💡 <strong>Insight:</strong> Smokers have much higher average insurance charges than
non-smokers, making smoking status a major cost-driving factor.
</div>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------
# Graph 3
# -----------------------------
st.header("3. BMI vs Insurance Charges")

fig3 = px.scatter(
    df,
    x="bmi",
    y="charges",
    color="smoker",
    title="BMI vs Insurance Charges",
    labels={"bmi": "BMI", "charges": "Insurance Charges", "smoker": "Smoker"}
)
fig3.update_layout(height=500, plot_bgcolor="white", paper_bgcolor="white")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
<div class="card">
💡 <strong>Insight:</strong> Higher BMI is generally associated with higher charges,
especially among smokers.
</div>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------
# Graph 4
# -----------------------------
st.header("4. Average Charges by Region")

region_avg = (
    df.groupby("region")["charges"]
    .mean()
    .reset_index()
    .sort_values("charges", ascending=False)
)

fig4 = px.bar(
    region_avg,
    x="region",
    y="charges",
    title="Average Charges by Region",
    labels={"region": "Region", "charges": "Average Charges"}
)
fig4.update_layout(height=460, plot_bgcolor="white", paper_bgcolor="white")
st.plotly_chart(fig4, use_container_width=True)

st.markdown("""
<div class="card">
💡 <strong>Insight:</strong> Regional differences exist, but they are much smaller
than the effect of smoking status.
</div>
""", unsafe_allow_html=True)

st.divider()

st.header("Overall Takeaway")

st.markdown("""
<div class="card">
<strong>Smoking status</strong> shows the strongest visual relationship with insurance charges.
<strong>BMI</strong> also shows a positive relationship with charges, especially for smokers.
<strong>Region</strong> has some effect, but it is less important than lifestyle-related factors.
</div>
""", unsafe_allow_html=True)