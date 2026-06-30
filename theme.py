import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    .stApp {
        background-color: #F5FAFF;
    }

    h1 {
        color: #1565C0;
        font-weight: 800;
    }

    h2, h3 {
        color: #1976D2;
    }

    [data-testid="stSidebar"] {
        background-color: #E3F2FD;
    }

    div[data-testid="stMetric"] {
        background-color: white;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #BBDEFB;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    .stButton > button {
        background-color: #1976D2;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.6rem 1rem;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #0D47A1;
        color: white;
    }

    div[data-testid="stDataFrame"] {
        background-color: white;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)