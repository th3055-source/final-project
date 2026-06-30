import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("insurance.csv")

st.title("📊 Data Visualization")

st.write(
    "This page explores the medical insurance dataset through different visualizations."
)

# -------------------------------
# Chart 1
# -------------------------------
st.header("Distribution of Insurance Charges")

fig, ax = plt.subplots(figsize=(8,5))
ax.hist(df["charges"], bins=30)
ax.set_xlabel("Charges")
ax.set_ylabel("Frequency")

st.pyplot(fig)

# -------------------------------
# Chart 2
# -------------------------------
st.header("Average Charges by Smoker")

avg_smoker = df.groupby("smoker")["charges"].mean()

fig, ax = plt.subplots(figsize=(6,4))
ax.bar(avg_smoker.index, avg_smoker.values)
ax.set_xlabel("Smoker")
ax.set_ylabel("Average Charges")

st.pyplot(fig)

# -------------------------------
# Chart 3
# -------------------------------
st.header("Average Charges by Region")

avg_region = df.groupby("region")["charges"].mean()

fig, ax = plt.subplots(figsize=(7,4))
ax.bar(avg_region.index, avg_region.values)
ax.set_xlabel("Region")
ax.set_ylabel("Average Charges")

st.pyplot(fig)

# -------------------------------
# Chart 4
# -------------------------------
st.header("BMI vs Insurance Charges")

fig, ax = plt.subplots(figsize=(7,5))
ax.scatter(df["bmi"], df["charges"])
ax.set_xlabel("BMI")
ax.set_ylabel("Charges")

st.pyplot(fig)