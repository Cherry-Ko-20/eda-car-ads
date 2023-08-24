import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st 
import plotly.express as px
import numpy as np
from PIL import Image 
import scipy as sp
import seaborn as sns 

spotify_genre = pd.read_csv('genres_v2.csv')
spotify_playlist= pd.read_csv('playlists.csv')
print(spotify_genre)
print(spotify_playlist)

spotify_genre.info()
spotify_playlist.info()

duplicate_genre= spotify_genre.duplicated().sum()
print(duplicate_genre)
duplicate_playlist=spotify_playlist.duplicated().sum()
print(duplicate_playlist)

missing_genre=spotify_genre.isnull().sum()
print(missing_genre)
missing_playlist= spotify_playlist.isnull().sum()
print(missing_playlist)
spotify_genre= spotify_genre.drop(columns= ["Unnamed: 0"])
print(spotify_genre)


#Streamlit app
st.header('Spotify Genre Analysis')


#Scatter plot or histogram based on checkbox value 
st.subheader('Scatter Plot: Danceability vs Energy')
scatter_fig = px.scatter(spotify_genre, x = 'danceability', y= 'energy', color='genre')
st.plotly_chart(scatter_fig)

st.subheader('Histogram: Danceability')
histogram_fig= px.histogram(spotify_genre, x = 'danceability', color= 'genre', marginal='rug')
st.plotly_chart(histogram_fig)


selected_genre = st.selectbox('Select Genre for Histogram', spotify_genre['genre'].unique())
filtered_data = spotify_genre[spotify_genre['genre'] == selected_genre]


st.subheader(f'Histogram: Danceability for {selected_genre}')
histogram_fig = px.histogram(filtered_data, x='danceability', marginal='rug', 
                             color_discrete_sequence=['lightblue'],
                             opacity=0.7, 
                             barmode='overlay',
                             barnorm='percent',
                             title=f'Histogram: Danceability for {selected_genre}')
histogram_fig.update_traces(marker_line_color='black', marker_line_width=1)
st.plotly_chart(histogram_fig)

selected_genre_scatter = st.selectbox('Select Genre for Scatter Plot', spotify_genre['genre'].unique())
filtered_data_scatter = spotify_genre[spotify_genre['genre'] == selected_genre_scatter]

selected_columns = st.multiselect('Select Columns for Scatter Plot', spotify_genre.columns)

if len(selected_columns) == 2:  
    scatter_data = filtered_data_scatter[selected_columns]
    x_column, y_column = selected_columns
    
    # Scatter plot
    st.subheader(f'Scatter Plot: {x_column} vs {y_column} for {selected_genre_scatter}')
    scatter_fig = px.scatter(scatter_data, x=x_column, y=y_column)
    st.plotly_chart(scatter_fig)
else:
    st.warning('Select exactly 2 columns for the scatter plot')