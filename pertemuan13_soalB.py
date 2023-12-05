import streamlit as st
import pandas as pd

df_anime = pd.read_csv("anime.csv")
st.image('komisan.jpg')
st.markdown("# IMDb Rating Count Anime Series")
pilihan = st.sidebar.selectbox("select column",df_anime.columns)
st.dataframe(df_anime[pilihan])
