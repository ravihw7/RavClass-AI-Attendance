import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

def main():
    style_base_layout()
    style_background_dashboard()
    st.title("Teacher Screen")