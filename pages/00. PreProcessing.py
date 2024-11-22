import streamlit as st
import pandas as pd
import plotly.express as px

# this change need
file_path = "../Restaurant_Ratings.xlsx"
st.title("PreProcessing")

ratings_df = pd.read_excel(file_path, sheet_name=0)
details_df = pd.read_excel(file_path, sheet_name=1)

# Display columns for ratings_df
st.header("Columns in Restaurant Ratings")
st.write("**Columns:**", ratings_df.columns.tolist())  # Display columns

# Display columns for details_df
st.header("Columns in Restaurant Details")
st.write("**Columns:**", details_df.columns.tolist())  # Display columns

st.write("Merging two tables based on Restaurant_ID")
st.write("Dropping column Name of Restaurant Details as we already have Restaurant_Name in Restaurant Ratings")

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
- 0 → "Don't Like"
- 1 → "Okay"
- 2 → "I like it"
""")

merged_df['Overall_Rating'].replace({
    0: "Don't Like",
    1: "Okay",
    2: "I like it"
}, inplace=True)


st.dataframe(merged_df)

st.write("Saving this dataframe to csv for further use.")
# merged_df.to_csv("merged_df.csv", index=False)
# commenting this code
