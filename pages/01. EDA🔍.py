import streamlit as st
import pandas as pd
import plotly.express as px


# File_path
file_path = "merged_df.csv"


st.title("🔍 Exploring the data")
merged_df = pd.read_csv(file_path)

filter_cuisine = st.sidebar.checkbox("Filter by Cuisine", value=False)
filter_price = st.sidebar.checkbox("Filter by Price", value=False)
filter_franchise = st.sidebar.checkbox("Filter by Franchise", value=False)


# Sidebar inputs
st.sidebar.title("Filter Options")

if filter_cuisine:
    # Cuisine input: Dropdown
    cuisines = merged_df['Cuisine'].unique()
    selected_cuisine = st.sidebar.selectbox("Select Cuisine", options=cuisines)
else:
    selected_cuisine = ''

if filter_price:
    # Cuisine input: Dropdown
    prices = merged_df['Price'].unique()
    selected_price = st.sidebar.selectbox("Select Price", options=prices)
else:
    selected_price = ''

if filter_franchise:
    # Franchise input: Checkbox
    franchise_options = merged_df['Franchise'].unique()
    selected_franchise = st.sidebar.radio(
        "Select Franchise Status", options=franchise_options)
else:
    filter_franchise = ''

# Display filter selections
if filter_cuisine:
    st.write(f"**Cuisine Selected**: `{selected_cuisine}`")
if filter_price:
    st.write(f"**Price Selected**: `{selected_price}`")
if filter_franchise:
    st.write(f"**Franchise Status**: `{selected_franchise}`")

filtered_df = merged_df
if filter_cuisine and selected_cuisine:
    filtered_df = filtered_df[filtered_df['Cuisine'] == selected_cuisine]

if filter_price and selected_price:
    filtered_df = filtered_df[filtered_df['Price'] == selected_price]

if filter_franchise and selected_franchise:
    filtered_df = filtered_df[filtered_df['Franchise'] == selected_franchise]

# Show filtered dataframe
st.write("### Filtered DataFrame", filtered_df)

value_counts = merged_df['Franchise'].value_counts().reset_index()
value_counts.columns = ['Franchise', 'count']

# Create the pie chart
fig = px.pie(
    value_counts,
    names='Franchise',
    values='count',
    title='Franchise or Independent? Restaurant Distribution in the Market 🏢',
    hover_data=['count'],  # Display counts on hover
)

# Update layout to show values 
fig.update_layout(
    xaxis_title=None,  # Remove X-axis label
    yaxis_title=None,  # Remove Y-axis label
    title_font_size=22,  # Bigger font size for the title
    font=dict(size=16),  # Adjust font size
    showlegend=True,
    legend=dict(
        font=dict(size=16),  # Increase legend font size
    ),
    xaxis_showgrid=False,  # Remove vertical gridlines
    yaxis_showgrid=False,  # Remove horizontal gridlines
    plot_bgcolor="white",  # Set background to white for a clean look
    

)



# Show the pie chart in Streamlit
st.plotly_chart(fig)


value_counts = merged_df['Price'].value_counts().reset_index()
value_counts.columns = ['Price', 'count']

# Create the pie chart
fig = px.pie(
    value_counts,
    names='Price',
    values='count',
    title='How Restaurants are Priced: Low, Medium, or High 💲',
    hover_data=['count'],  # Display counts on hover
)

# Update layout to show values 
fig.update_layout(
    xaxis_title=None,  # Remove X-axis label
    yaxis_title=None,  # Remove Y-axis label
    title_font_size=22,  # Bigger font size for the title
    font=dict(size=16),  # Adjust font size
    showlegend=True,
    legend=dict(
        font=dict(size=16),  # Increase legend font size
    ),
    xaxis_showgrid=False,  # Remove vertical gridlines
    yaxis_showgrid=False,  # Remove horizontal gridlines
    plot_bgcolor="white",  # Set background to white for a clean look
    

)




# Show the pie chart in Streamlit
st.plotly_chart(fig)


st.write("Discover fresh tips and recommendations for the best cuisines")
number_of_cuisines = st.number_input(
    "✨ Want to see the most popular cuisines? Adjust the number below to explore top-rated options:",
    min_value=1,
    max_value=len(merged_df["Cuisine"].unique()),
    value=5,
    step=1,
)

# Count the occurrences of each cuisine
cuisine_counts = merged_df['Cuisine'].value_counts().reset_index()
cuisine_counts.columns = ['Cuisine', 'count']

# Get the top 'n' cuisines
top_cuisines = cuisine_counts.head(number_of_cuisines)

# Create a bar chart
fig = px.bar(
    top_cuisines,
    x='Cuisine',
    y='count',
    title=f"Top {number_of_cuisines} Cuisines",
    #text='count',  # Display counts on the bars
    hover_data={"count": True} , # Enable tooltips for count
    labels={'Cuisine': 'Cuisine', 'count': 'Count'}
)

# Update layout to show values on bars
fig.update_traces(textposition='outside')
fig.update_layout(
    xaxis_title=None,  # Remove X-axis label
    yaxis_title=None,  # Remove Y-axis label
    title_font_size=22,  # Bigger font size for the title
    font=dict(size=16),  # Adjust font size
    xaxis_showgrid=False,  # Remove vertical gridlines
    yaxis_showgrid=False,  # Remove horizontal gridlines
    plot_bgcolor="white",  # Set background to white for a clean look

)

# Ensure tooltips appear on hover
fig.update_traces(
    hovertemplate="<b>Cuisine: %{x}</b><br>Count: %{y}<extra></extra>",
    text=None  # Remove direct text labels on the bars
)


# Remove data labels
#fig.update_traces(text=None)


# Optionally hide tick marks (if needed)
fig.update_xaxes(showticklabels=True)
fig.update_yaxes(showticklabels=False)



# Display the bar chart in Streamlit
st.plotly_chart(fig)


value_counts = merged_df['Overall_Rating'].value_counts().reset_index()
value_counts.columns = ['Overall_Rating', 'count']

# Create the pie chart
fig = px.pie(
    value_counts,
    names='Overall_Rating',
    values='count',
    title='Restaurant Feedback Overview: Love It or Leave It?🍽️',
    hover_data=['count'],  # Display counts on hover
)

# Update layout to show values 
fig.update_layout(
    xaxis_title=None,  # Remove X-axis label
    yaxis_title=None,  # Remove Y-axis label
    title_font_size=22,  # Bigger font size for the title
    font=dict(size=16),  # Adjust font size
    showlegend=True,
    legend=dict(
        font=dict(size=16),  # Increase legend font size
    ),
    xaxis_showgrid=False,  # Remove vertical gridlines
    yaxis_showgrid=False,  # Remove horizontal gridlines
    plot_bgcolor="white",  # Set background to white for a clean look
    

)



# Show the pie chart in Streamlit
st.plotly_chart(fig)




