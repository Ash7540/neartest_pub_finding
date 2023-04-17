import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static


# Load the dataset
df = pd.read_csv('pubs_updated.csv')

# Create the Pub Locations Page
def pub_location_page():
    st.title('Pub Locations')
    st.write('Enter the Postal Code or Local Authority to find pubs in the area')
    searchType = st.selectbox('Search by', ('Postal Code', 'Local Authority'))
    if searchType == 'Postal Code':
        postCode = st.text_input('Enter the Postal Code')
        pubs = df[df['postcode'] == postCode]
    else:
        localAuthority = st.text_input('Enter the Local Authority')
        pubs = df[df['local_authority'] == localAuthority]
    
    # Display the map
    if len(pubs) > 0:
        a = folium.Map(location=[pubs['latitude'].mean(),pubs['longitude'].mean()], zoom_start=13)
        for index, row in pubs.iterrows():
            folium.Marker(location=[row['latitude'], row['longitude']], popup=row['name']).add_to(a)
        folium_static(a)
    else:
        st.write('No pubs found in the selected area')

# Run the app
if __name__ == '__main__':
    pub_location_page()
