import json
from streamlit_lottie import st_lottie
import streamlit as st


# Function to load local JSON animation files
def load_lottiefile(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


# Function to load portfolio data
def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


# Load portfolio data
portfolio_data = load_json("assets/portfolio.json")

# Display portfolio
st.title("Antuan's Portfolio")

for entry in portfolio_data:
    col1, col2 = st.columns([1, 2])

    # Display animation in left column
    with col1:
        animation_path = entry.get("animation")
        if animation_path:
            animation_data = load_lottiefile(animation_path)
            st_lottie(animation_data, height=150)
        else:
            st.warning("No animation available.")

    # Display content in right column
    with col2:
        st.subheader(entry["title"])
        st.write(entry["description"])
        st.video(entry["video"])
