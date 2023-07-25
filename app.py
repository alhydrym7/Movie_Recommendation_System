
import streamlit as st
from PIL import Image
import pandas as pd
import pickle
import requests

image2 = Image.open(r"C:\Users\asus\Downloads\logo.ico")
st.sidebar.image(image2)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie, df):
    index = df[df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = df.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(df.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


st.sidebar.info('مرحبًا بك في نظام توصية الأفلام.')
st.sidebar.info("تم إنشاء وتصميمه بواسطة فريق K-Digital")

page = st.sidebar.selectbox("كيف ترغب في البحث؟", ["الصفحة الرئيسية", "عن طريق التشابه", "عن طريق المعلومات"])

if page == "الصفحة الرئيسية":
    st.header('مرحبًا بك في نظام توصية الأفلام')
    st.write("<span style='font-family: Arial; color: #C4CA02; font-size: 45px;'>تم التصميم بواسطة: </span>", unsafe_allow_html=True)
    st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>1. محمد عادل</span>", unsafe_allow_html=True)
    st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>2. عبدالرحمن خالد </span>", unsafe_allow_html=True)
    st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>3. شهد محمد </span>", unsafe_allow_html=True)
    st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>4. إكرام فراس </span>", unsafe_allow_html=True)
    st.write("<span style='font-family: Arial; color: #C4CA02; font-size: 35px;'>هذا المشروع تحت إشراف:</span>", unsafe_allow_html=True)
    st.write("<span style='text-align: center: Arial; color: #94E6E6; font-size: 45px;'>الأستاذة مروى </span>", unsafe_allow_html=True)

if page == "عن طريق التشابه":
    st.header('نظام توصية الأفلام')
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    

    movie_list = movies['title'].values
    selected_movie = st.selectbox("اختر الفيلم من القائمة", movie_list)

    if st.button('عرض التوصيات'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie, movies)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0], use_column_width=True)


        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1], use_column_width=True)


        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2], use_column_width=True)


if page == "عن طريق المعلومات":
    st.header("معلومات الفيلم")

    program = pd.read_pickle("program.pkl")

    quality = st.text_input("أدخل جودة الفيلم (SD أو HD):").upper()
    genre = st.text_input("أدخل التصنيف المطلوب:")
    film_or_series = st.text_input("هل تبحث عن فلم أم مسلسل (S أو M):").upper()
    num = st.text_input("ادخل عدد التوصيات التي تريدها:")

   
    if st.button("البحث"):
    
        if num:
            num = int(num)
        else:
            num = 5  

        quality_value = 1 if quality == "HD" else 0
        film_or_series = "movie" if film_or_series == "F" else "series"
        filtered_data = program[
            (program["genre"] == genre) &
            (program["type"] == film_or_series) &
            (program["hd"] == quality_value)
        ]
        filtered_data = filtered_data.sort_values(by='number_of_watches', ascending=False)
        filtered_data = filtered_data[["type", "genre", "name", "number_of_watches"]]
        st.dataframe(filtered_data.head(num))


st.markdown(
    """
    <style>
    body {
        direction: rtl;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True,
)






