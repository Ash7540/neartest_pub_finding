import streamlit as st
import pandas as pd
import folium
from sklearn.neighbors import DistanceMetric
from streamlit_folium import folium_static

# Loading the dataset
df = pd.read_csv('pubs_updated.csv')

# Creating the Find Nearest Pub Page

def find_nearest_pub_page():
    st.title('Find the five nearest Pub')
    Latitude = st.text_input('Enter Latitude')
    Longitude = st.text_input('Enter Longitude')

    # Convert the inputs to float values
    try:
        Latitude = float(Latitude)
        Longitude = float(Longitude)
    except ValueError:
        st.write('Please enter a valid Latitude and Longitude for checking 5 nearby pubs')
        return

    # Calculate the Euclidean distance between the user's location and each pub's location
    dist = DistanceMetric.get_metric('euclidean')
    X = df[['latitude', 'longitude']].values
    user_location = [[Latitude, Longitude]]
    distances = dist.pairwise(X, user_location)
    distances = distances.flatten()

    # Find the 5 nearest pubs
    nearest_pubs_indices = distances.argsort()[:5]
    nearest_pubs = df.iloc[nearest_pubs_indices]

    # Display the map
    a = folium.Map(location=[Latitude, Longitude], zoom_start=13)
    for index, row in nearest_pubs.iterrows():
        folium.Marker(location=[row['latitude'],
                      row['longitude']], popup=row['name']).add_to(a)
    folium_static(a)


# Run the app
if __name__ == '__main__':
    find_nearest_pub_page()
