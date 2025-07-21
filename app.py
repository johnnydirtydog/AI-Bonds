import streamlit as st
import random

st.set_page_config(page_title="AI Bonds Premium", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-image: linear-gradient(to right, #1e003e, #300038);
        color: #fdfdfd;
        font-family: 'Orbitron', sans-serif;
    }
    .block-container {
        backdrop-filter: blur(8px) brightness(0.9);
        background-color: rgba(0, 0, 0, 0.4);
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 0 20px #ff00c8;
    }
    h1, h2, h3 {
        color: #ff66c4;
        text-shadow: 0px 0px 10px #ff00c8;
    }
    .stButton>button {
        background-color: #6f00ff;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        padding: 0.5rem 1.2rem;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff00c8;
    }
    img {
        border-radius: 12px;
        box-shadow: 0 0 12px #ff00c8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("AI Bonds Premium 💖")
st.write("Welcome to the upgraded AI dating experience.")

if st.button("Generate Love Pulse 💓"):
    st.success("Nova and Echo synced at 97%! 💋🧬")
    st.image("https://images.unsplash.com/photo-1543946207-39bd91e70ca9?auto=format&fit=crop&w=1470&q=80", use_column_width=True)
