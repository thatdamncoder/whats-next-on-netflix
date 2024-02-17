import streamlit as st
import pickle
import os
import pandas as pd
import requests

st.set_page_config(page_title="WhatsNextOnNetflix",page_icon="🐞",layout="wide")

page_bg="""
    <style>
    [data-testid='stAppViewContainer']{
    background-image: url("https://maven-uploads.s3.amazonaws.com/120386748/projects/netflix%20image.jpg");
    background-size: cover;
    }
    [data-testid='stHeader']{
    background-image: url("https://maven-uploads.s3.amazonaws.com/120386748/projects/netflix%20image.jpg");
    background-size: cover;
    }
    </style>
"""

st.markdown(page_bg,unsafe_allow_html=True)

api_key=os.getenv("API_KEY")
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie_id,api_key))
    data=response.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:11]
    recmovies=[]
    recmoviesposter=[]
    for i in distances:
        movie_id=movies.iloc[i[0]].movie_id
        recmovies.append(movies.iloc[i[0]].title)
        recmoviesposter.append(fetch_poster(movie_id))
    return recmovies,recmoviesposter

movieDict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movieDict)
similarity=pickle.load(open('similarity.pkl','rb'))


# header,signin=st.columns([3,3])
st.markdown("<h1 style='text-align: left; color: red;font-size: 300%;font-weight:900;'>NETFLIX</h1>", unsafe_allow_html=True)
# with signin:
#     st.markdown("<h4 style='text-align: right; color: red;'>What's next on Netflix?</h1>", unsafe_allow_html=True)
st.divider()
st.markdown("<h1 style='text-align: center; color: white;font-size: 400%;font-weight:bold;'>What's Next on Netflix?</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;font-weight:bold;'>Pick up or type down your fav movie and see what's next!</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: left; color: white;font-weight:bold;'>What do you want us to recommend?</h1>", unsafe_allow_html=True)
# st.markdown("<h3 style='text-align: center; color: white;font-weight:bold;'>Be Patient! The fetching may take a few seconds</h1>", unsafe_allow_html=True)
st.markdown('Be Patient! The fetching may take a few seconds')

selected_movie = st.selectbox('', movies['title'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_movie)
    i = 0
    for j in range(2):
        col1,col2,col3,col4,col5=st.columns([1,1,1,1,1])
        with col1:
            st.text(names[i])
            st.image(posters[i])
            i+=1
        with col2:
            st.text(names[i])
            st.image(posters[i])
            i+=1
        with col3:
            st.text(names[i])
            st.image(posters[i])
            i+=1
        with col4:
            st.text(names[i])
            st.image(posters[i])
            i+=1
        with col5:
            st.text(names[i])
            st.image(posters[i])
            i+=1





