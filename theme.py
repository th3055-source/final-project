import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #EAF4FF 0%, #F8FBFF 100%);
    }

    [data-testid="stSidebar"] {
        background-color: #DCEEFF;
    }

    [data-testid="block-container"] {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1 {
        color: #0D47A1;
        font-weight: 800;
    }

    h2, h3 {
        color: #1565C0;
        font-weight: 700;
    }

    .card {
        background-color: white;
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #BBDEFB;
        box-shadow: 0 4px 14px rgba(25, 118, 210, 0.12);
        margin-bottom: 18px;
    }

    .small-card {
        background-color: white;
        padding: 18px;
        border-radius: 16px;
        border: 1px solid #BBDEFB;
        text-align: center;
        box-shadow: 0 3px 10px rgba(25, 118, 210, 0.10);
    }

    .metric-number {
        font-size: 34px;
        font-weight: 800;
        color: #0D47A1;
    }

    .metric-label {
        font-size: 15px;
        color: #455A64;
    }

    .stButton > button {
        background-color: #1976D2;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: 700;
    }

    .stButton > button:hover {
        background-color: #0D47A1;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)