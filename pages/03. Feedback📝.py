import streamlit as st
import pandas as pd
import os

# this need change
folder_path = r"C:\Users\natas\Downloads\app\app\pages"

st.title("📝 Feedback")
st.write("Please provide your feedback.")


# Function to save or append to feedback.csv
def save_feedback(folder_path, name, feedback):
    # Define the path to the feedback.csv file
    file_path = os.path.join(folder_path, 'feedback.csv')

    # Check if the file exists
    if os.path.exists(file_path):
        # If the file exists, read it and append the new feedback
        df = pd.read_csv(file_path)
        new_row = pd.DataFrame({'name': [name], 'feedback': [feedback]}, index=[len(df)])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(file_path, index=False)  # Save back to the file
    else:
        # If the file doesn't exist, create it and save the first row
        new_row = {'name': name, 'feedback': feedback}
        df = pd.DataFrame([new_row])
        df.to_csv(file_path, index=False)  # Create the new file and save data


# Get inputs from the user
name = st.text_input('Enter your name:')
feedback = st.text_area('Enter your feedback:')

# Button to submit feedback
if st.button('Submit Feedback'):
    if name and feedback and folder_path:
        # Save or append the feedback data
        save_feedback(folder_path, name, feedback)
        st.success('Feedback submitted successfully!')
    else:
        st.error('Please fill all the fields!')
