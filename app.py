import streamlit as st
import pickle
import pandas as pd

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies_dict=movies_list['title'].values
movies=pd.DataFrame(movies_dict)

st.title('Movie Recommendation System')

options=st.selectbox('Movies you want to watch?',
                     movies['title'].values)