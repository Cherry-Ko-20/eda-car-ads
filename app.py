import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st 
import plotly.express as px

spotify_genre=pd.read_csv('./csvFiles/genres_v2.csv')
spotify_playlist= pd.read_csv('./csvFiles/playlists.csv')
print(spotify_genre)
print(spotify_playlist)