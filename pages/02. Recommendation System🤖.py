import pandas as pd
import numpy as np
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer


# this need change
file_path = "merged_df.csv"

st.title("🤖 Recommendation System")
st.write("Welcome to Restaurant Recomendation Sytem")


def preprocess_ratings(df):
    # Map ratings into categories: don't like (0), okay (1), I like it (2)
    rating_map = {'don\'t like': 0, 'okay': 1, 'I like it': 2}
    df['Overall_Rating'] = df['Overall_Rating'].map(rating_map)
    return df


def preprocess_features(df):
    # Label encoding for 'Price' and 'Franchise'
    price_mapping = {'low': 1, 'medium': 2, 'high': 3, 'none': 0}
    franchise_mapping = {'no': 1, 'yes': 2, 'none': 0}

    df['Price'] = df['Price'].map(price_mapping)
    df['Franchise'] = df['Franchise'].map(franchise_mapping)

    # One-hot encoding for 'Cuisine' (22 unique categories)
    cuisine_encoder = OneHotEncoder()
    cuisine_encoded = cuisine_encoder.fit_transform(df[['Cuisine']])
    cuisine_encoded_df = pd.DataFrame(cuisine_encoded)

    # Combine the encoded features with the original dataframe
    df = pd.concat([df, cuisine_encoded_df], axis=1)
    # Drop the original 'Cuisine' column
    df.drop('Cuisine', axis=1, inplace=True)

    return df, cuisine_encoder

# Content-based similarity (based on price, franchise, and cuisine)


def collaborative_filtering(df, n, method='user'):
    # Create user-item matrix for collaborative filtering
    user_item_matrix = df.pivot_table(
        index='Consumer_ID', columns='Restaurant_ID', values='Overall_Rating', aggfunc='mean')

    # Fill missing values with 0
    user_item_matrix = user_item_matrix.fillna(0)

    if method == 'user':
        # User-based collaborative filtering (cosine similarity between users)
        cosine_sim = cosine_similarity(user_item_matrix)
        np.fill_diagonal(cosine_sim, 0)  # Remove self-similarity

        return cosine_sim
    elif method == 'item':
        # Item-based collaborative filtering (cosine similarity between items)
        # Transpose to get item-item similarities
        cosine_sim = cosine_similarity(user_item_matrix.T)
        np.fill_diagonal(cosine_sim, 0)

        return cosine_sim


def recommend_restaurants(df, restaurant_id, n, method='user'):
    if method == 'user':
        # User-based Collaborative Filtering
        cosine_sim = collaborative_filtering(df, n, method='user')
        idx = df[df['Restaurant_ID'] == restaurant_id].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))

        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[:n]
        restaurant_indices = [x[0] for x in sim_scores]

    elif method == 'item':
        # Item-based Collaborative Filtering
        cosine_sim = collaborative_filtering(df, n, method='item')
        idx = df[df['Restaurant_ID'] == restaurant_id].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))

        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[:n]
        restaurant_indices = [x[0] for x in sim_scores]

    return df.iloc[restaurant_indices]


def run_app():
    st.title("Restaurant Recommender System")

    # Preprocess the dataset
    merged_df = pd.read_csv(file_path)
    rest_dict = dict(
        zip(merged_df['Restaurant_Name'], merged_df['Restaurant_ID']))
    df_processed = merged_df.copy()
    df_processed = preprocess_ratings(df_processed)
    df_processed, cuisine_encoder = preprocess_features(df_processed)

    # User Input for the number of similar restaurants
    n = st.number_input("Enter the number of similar restaurants to recommend",
                        min_value=1, max_value=20, value=5)

    # Choose the method for filtering
    method = st.selectbox("Select Filtering Method", [
                          'user', 'item'])

    restaurant_name = st.selectbox(
        "Select Restaurant Name", df_processed['Restaurant_Name'].unique()
    )

    similar_restaurants = recommend_restaurants(
        df_processed, rest_dict[restaurant_name], n, method=method)

    st.subheader("Recommended Restaurants:")
    st.write(similar_restaurants[['Restaurant_Name',
             'Overall_Rating', 'Price', 'Franchise']])


if __name__ == "__main__":
    run_app()
