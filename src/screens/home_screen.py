import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import base_layout

def home_screen():

    header_home()
    base_layout()
    col1, col2 =st.columns(2) 
    with col1:
        if st.button("Teacher Login"):
            st.session_state['login_type'] = "teacher"
            st.rerun()
    with col2:
        if st.button("Student Login"):
            st.session_state['login_type'] = "student"
            st.rerun()
