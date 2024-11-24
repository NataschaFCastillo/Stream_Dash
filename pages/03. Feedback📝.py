import streamlit as st
import pandas as pd
import os

# this need change
folder_path = "pages"

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
st.write("Did you enjoy your recommendation?")
yes_button_clicked = st.button("👍Yes!")
no_button_clicked = st.button("👎No!")

if yes_button_clicked:
    st.write("Glad you enjoyed it!?")
elif no_button_clicked:
    st.write("We're sorry to hear that. We'll strive to improve.")

experiene_rating = st.slider("On a scale of 1 to 10, how would you rate your experience today?", 1, 10, 5)

# Get inputs from the user
st.write("We value your feedback. Please tell us more about your experience?")
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
