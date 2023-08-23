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


spotify_genre.hist(figsize=(12, 10))
plt.tight_layout()
plt.show()


# Correlation heatmap
correlation_matrix = spotify_genre.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

