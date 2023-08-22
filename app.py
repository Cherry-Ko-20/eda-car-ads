import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st 
import plotly.express as px
import numpy as np

spotify_genre=pd.read_csv('genres_v2.csv')
spotify_playlist= pd.read_csv('playlists.csv')
print(spotify_genre)
print(spotify_playlist)