import streamlit as st
import pandas as pd
import plotly.express as px

# File_path
file_path = "Restaurant_Ratings.xlsx"

# Title with Icon and Custom Font Size
st.markdown("<h1 style='font-size:36px;'>⏳ PreProcessing</h1>", unsafe_allow_html=True)
# Description with Slightly Smaller Font and Custom Styling
st.markdown("<p style='font-size:18px;'>A summary of the steps made during the preprocessing step</p>", unsafe_allow_html=True)


ratings_df = pd.read_excel(file_path, sheet_name=0)
details_df = pd.read_excel(file_path, sheet_name=1)

# Display columns for ratings_df
#st.header("Sheet Restaurant Ratings")
st.markdown("## Table Restaurant Ratings")
st.write("**We have 4 columns below:**", ratings_df.columns.tolist())  # Display columns

# Display columns for details_df
st.header("Table Restaurant Details")
st.write("**We have 5 Columns below:**", details_df.columns.tolist())  # Display columns

#st.title("Steps done in PreProcessing")
st.markdown("### Steps done in PreProcessing")
st.write("1. Merging two tables based on Restaurant_ID")
st.write("2. Dropping column Name of Restaurant Details as we already have Restaurant_Name in Restaurant Ratings")

merged_df = pd.merge(ratings_df, details_df, on="Restaurant_ID", how="left")
merged_df.drop(columns=["Name"], inplace=True)

cuisine_null_count = merged_df["Cuisine"].isna().sum()
price_null_count = merged_df["Price"].isna().sum()
franchise_null_count = merged_df["Franchise"].isna().sum()

st.write("Total Records :", merged_df.shape[0])

st.write("Null Values in Cuisine: ", cuisine_null_count)
st.write("Null Values in Price: ", price_null_count)
st.write("Null Values in Franchise: ", franchise_null_count)

st.write("Filling Null Values in Cuisine with : `Not Informed`")
merged_df['Cuisine'].fillna("Not Informed", inplace=True)
st.write("Filling Null Values in Franchise and Price with : `None`")
merged_df['Franchise'].fillna("None", inplace=True)
merged_df['Price'].fillna("None", inplace=True)


st.write("""
### Transformation Applied:
Replaced the values in the `Overall_Rating` column as follows:
- 0 → "Don't Like it"
- 1 → "I like it"
- 2 → "I love it"
""")

merged_df['Overall_Rating'].replace({
    0: "Don't Like it",
    1: "I like it",
    2: "I love it"
}, inplace=True)


st.dataframe(merged_df)

st.write("Saving this dataframe to csv for further use.")
# merged_df.to_csv("merged_df.csv", index=False)
# commenting this code
