import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5YjkyOTA5OGI0NmY3ODZlNmIwZWJlMzAxODc3OGNlNCIsIm5iZiI6MTc2NDM0ODk3MS4xNTgwMDAyLCJzdWIiOiI2OTI5ZDQyYmEyYjQ3YWIwYTJjMTI5OWYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.8TQihaAzmQFb6KVm7_YgW0awqAxgxOoxEgws8bjSx1k"
    }

    url=f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error fetching poster:", response.text)
        return None

    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']




def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        tmdb_id=movies.iloc[i[0]].id
        #fetching poster from API
        recommended_movies.append(movies.iloc[i[0]]['title'])
        recommended_movies_posters.append(fetch_poster(tmdb_id))
    return recommended_movies,recommended_movies_posters

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

options=st.selectbox('Movies you want to watch?',
                     movies['title'].values)

if st.button('Recommend'):
    names,posters=recommend(options)

    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])