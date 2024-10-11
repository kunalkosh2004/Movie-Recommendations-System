import streamlit as st
import pickle
import requests

def poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend_movies(movie):
    movie_index = df[df['title']==movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), key=lambda x: x[1], reverse=True)[1:6]
    recommended_movies = []
    movies_poster = []
    for i in movie_list:
        movie_id = df.iloc[i[0]].movie_id
        movies_poster.append(poster(movie_id))
        recommended_movies.append(df.iloc[i[0]].title)
    return movies_poster,recommended_movies

st.title("Movie Recommendation System")

df = pickle.load(open('movies.pkl','rb'))
# movies_df = pd.DataFrame(df)

movies_list = df['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

select_movie = st.selectbox(
    "Which movie would you like to recommend?",(
        movies_list
    )
)
# st.dataframe(movies_list)
if st.button("Recommend"):
    poster,name = recommend_movies(select_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])



