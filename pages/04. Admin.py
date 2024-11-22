import streamlit as st
import pandas as pd

# this need change
file_path = r"C:\Users\natas\Downloads\app\app\pages\feedback.csv"

user_input = st.text_input("Enter Credential:")

if user_input == "admin":
    feedback = pd.read_csv(file_path)
    st.dataframe(feedback)
