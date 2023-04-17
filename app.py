import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Load the dataset
data = pd.read_csv('pubs_updated.csv')

# Calculate some basic statistics
total_pubs = len(data)
unique_postcodes = len(data['postcode'].unique())
unique_local_authorities = len(data['local_authority'].unique())

# Create the Home Page
def home_page():
    st.title('Welcome to the Ashu Pub Finder Website')
    st.write('This website will allow you to find pubs near you based on your location or on the longitude and latitude.')
    st.write('Here are some basic of statistics about the dataset:')
    st.write('Total number of pubs in the dataset:', total_pubs)
    st.write('Number of unique postcodes in the dataset:', unique_postcodes)
    st.write('Number of unique local authorities in the dataset:', unique_local_authorities)

    # Select the columns to display
    cols = ['fsa_id', 'name', 'address', 'postcode', 'easting',
            'northing', 'latitude', 'longitude', 'local_authority']

    # Create a selectbox to choose a Locality_Authority
    locality_authority = data['local_authority'].unique()
    selected_locality_authority = st.sidebar.selectbox(
        'Select a Locality_Authority', locality_authority)

    # Filter the data by the selected Locality_Authority
    filtered_data = data[data['local_authority']
                         == selected_locality_authority]

    # Display the filtered data in a table
    st.title(f'Pubs in {selected_locality_authority}')
    st.table(filtered_data[cols])

    # Create a map centered on the selected Locality_Authority
    center_lat = filtered_data['latitude'].mean()
    center_lon = filtered_data['longitude'].mean()
    m = folium.Map(location=[center_lat, center_lon], zoom_start=13)

    # Add markers for each pub in the filtered data
    for index, row in filtered_data.iterrows():
        folium.Marker(location=[row['latitude'], row['longitude']], popup=row['name']).add_to(m)
    # Display the map
    folium_static(m)

# Run the app
if __name__ == '__main__':
    home_page()
