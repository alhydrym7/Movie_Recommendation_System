# import pickle
# import streamlit as st
# import requests

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)

#     return recommended_movie_names,recommended_movie_posters


# st.header('Movie Recommender System')
# st.sidebar.info('Welcome to the Movie Recommender System.')
# st.sidebar.info("Created and designed by Mohammed Adil)")
# movies = pickle.load(open('movie_list.pkl','rb'))
# similarity = pickle.load(open('similarity.pkl','rb'))

# movie_list = movies['title'].values
# st.write(movies["tags"])
# selected_movie = st.selectbox("Type or select a movie from the dropdown",movie_list)

# if st.button('Show Recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])

#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])










# import pickle
# import streamlit as st
# import requests

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# def recommend(movie, df):
#     index = df[df['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = df.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(df.iloc[i[0]].title)

#     return recommended_movie_names, recommended_movie_posters

# def get_movie_score(title, df):
#     movie_row = df[df['title'] == title]
#     if movie_row.empty:
#         return None
#     score = movie_row['normalized_weighted_avg'] * 0.5 + movie_row['normalized_popularity'] * 0.5
#     return score.values[0]

# st.header('Movie Recommender System')
# st.sidebar.info('Welcome to the Movie Recommender System.')
# st.sidebar.info("Created and designed by Mohammed Adil)")
# movies = pickle.load(open('movie_list.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))
# score_df = pickle.load(open('score_df.pkl', 'rb'))

# movie_list = movies['title'].values
# selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# if st.button('Show Recommendation'):
#     recommended_movie_names, recommended_movie_posters = recommend(selected_movie, movies)
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0], use_column_width=True)
#         score = get_movie_score(recommended_movie_names[0], score_df)
#         score = score*100
#         score = round(score,2)
#         if score is not None:
#             st.text(f"Score: {score}%")

#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1], use_column_width=True)
#         score = get_movie_score(recommended_movie_names[1], score_df)
#         score = score*100
#         score = round(score,2)
#         if score is not None:
#             st.text(f"Score: {score}%")

#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2], use_column_width=True)
#         score = get_movie_score(recommended_movie_names[2], score_df)
#         score = score*100
#         score = round(score,2)
#         if score is not None:
#             st.text(f"Score: {score}%")















# import streamlit as st
# from PIL import Image
# import pandas as pd
# import pickle
# import requests


# image2 = Image.open(r"C:\Users\asus\Downloads\logo.ico")
# st.sidebar.image(image2)






# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# def recommend(movie, df):
#     index = df[df['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = df.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(df.iloc[i[0]].title)

#     return recommended_movie_names, recommended_movie_posters

# def get_movie_score(title, df):
#     movie_row = df[df['title'] == title]
#     if movie_row.empty:
#         return None
#     score = movie_row['normalized_weighted_avg'] * 0.5 + movie_row['normalized_popularity'] * 0.5
#     return score.values[0]

# st.sidebar.info('Welcome to the Movie Recommender System.')
# st.sidebar.info("Created and designed by K-Digital Team")



# page = st.sidebar.radio("How would you like to search?", options=["Home", "Recommended Movies"])

# if page == "Home":
#     st.header('Welcome to the Movie Recommender System')
    
#     st.write("<span style='font-family: Arial; color: #C4CA02; font-size: 45px;'>Created by: </span>", unsafe_allow_html=True)
    
#     st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>1. Mohammed Adel</span>", unsafe_allow_html=True)
#     st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>2. Abdulrahman Khaled </span>", unsafe_allow_html=True)
#     st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>3. Shahad Mohammed </span>", unsafe_allow_html=True)
#     st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>4. Ekram Feras </span>", unsafe_allow_html=True)
    
#     st.write("<span style='font-family: Arial; color: #C4CA02; font-size: 35px;'>This project is Under supervision:</span>", unsafe_allow_html=True)
#     st.write("<span style='text-align: center: Arial; color: #94E6E6; font-size: 45px;'>Ms. Marwa </span>", unsafe_allow_html=True)





# if page == "Recommended Movies":
#     st.header('Movie Recommender System')
#     movies = pickle.load(open('movie_list.pkl', 'rb'))
#     similarity = pickle.load(open('similarity.pkl', 'rb'))
#     score_df = pickle.load(open('score_df.pkl', 'rb'))


#     movie_list = movies['title'].values
#     selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

#     if st.button('Show Recommendation'):
#         recommended_movie_names, recommended_movie_posters = recommend(selected_movie, movies)
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.text(recommended_movie_names[0])
#             st.image(recommended_movie_posters[0], use_column_width=True)
#             score = get_movie_score(recommended_movie_names[0], score_df)
#             score = score*100
#             score = round(score,2)
#             # if score is not None:
#             #     st.text(f"Score: {score}%")

#         with col2:
#             st.text(recommended_movie_names[1])
#             st.image(recommended_movie_posters[1], use_column_width=True)
#             score = get_movie_score(recommended_movie_names[1], score_df)
#             score = score*100
#             score = round(score,2)
#             # if score is not None:
#             #     st.text(f"Score: {score}%")

#         with col3:
#             st.text(recommended_movie_names[2])
#             st.image(recommended_movie_posters[2], use_column_width=True)
#             score = get_movie_score(recommended_movie_names[2], score_df)
#             score = score*100
#             score = round(score,2)
#             if score is not None:
#                 st.text(f"Score: {score}%")















import streamlit as st
from PIL import Image
import pandas as pd
import pickle
import requests

# تحميل الصورة
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

    # عند الضغط على الزر، نقوم بتنفيذ البحث وعرض النتائج في جدول
    if st.button("البحث"):
        # التحقق من وجود قيمة غير فارغة قبل تحويلها إلى عدد صحيح
        if num:
            num = int(num)
        else:
            num = 5  # قيمة افتراضية في حالة عدم توفر قيمة من المستخدم

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

# إضافة أنماط CSS لتحقيق توجيه الصفحة من اليمين إلى اليسار
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








# import streamlit as st
# from PIL import Image
# import pandas as pd
# import pickle
# import requests


# image2 = Image.open(r"C:\Users\asus\Downloads\logo.ico")
# st.sidebar.image(image2)



# def Function_for_choose():
#     option = st.sidebar.selectbox('Choose A Summary Language', ['Home','Arabic','English'])

#     if option == 'Home':
#         home()


# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# def recommend(movie, df):
#     index = df[df['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = df.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(df.iloc[i[0]].title)

#     return recommended_movie_names, recommended_movie_posters

# def get_movie_score(title, df):
#     movie_row = df[df['title'] == title]
#     if movie_row.empty:
#         return None
#     score = movie_row['normalized_weighted_avg'] * 0.5 + movie_row['normalized_popularity'] * 0.5
#     return score.values[0]

# st.sidebar.info('Welcome to the Movie Recommender System.')
# st.sidebar.info("Created and designed by K-Digital Team")



# page = st.sidebar.radio("How would you like to search?", options=["Home", "Recommended Movies"])

# def home():
#     st.header('Welcome to the Movie Recommender System')
    
#     st.write("<span style='font-family: Arial; color: #C4CA02; font-size: 45px;'>Created by: </span>", unsafe_allow_html=True)
    
#     st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>1. Mohammed Adel</span>", unsafe_allow_html=True)
#     st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>2. Abdulrahman Khaled </span>", unsafe_allow_html=True)
#     st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>3. Shahad Mohammed </span>", unsafe_allow_html=True)
#     st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>4. Ekram Feras </span>", unsafe_allow_html=True)
    
#     st.write("<span style='font-family: Arial; color: #C4CA02; font-size: 35px;'>This project is Under supervision:</span>", unsafe_allow_html=True)
#     st.write("<span style='text-align: center: Arial; color: #94E6E6; font-size: 45px;'>Ms. Marwa </span>", unsafe_allow_html=True)




# def recommended():


#     st.header('Movie Recommender System')
#     movies = pickle.load(open('movie_list.pkl', 'rb'))
#     similarity = pickle.load(open('similarity.pkl', 'rb'))
#     score_df = pickle.load(open('score_df.pkl', 'rb'))


#     movie_list = movies['title'].values
#     selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

#     if st.button('Show Recommendation'):
#         recommended_movie_names, recommended_movie_posters = recommend(selected_movie, movies)
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.text(recommended_movie_names[0])
#             st.image(recommended_movie_posters[0], use_column_width=True)
#             score = get_movie_score(recommended_movie_names[0], score_df)
#             score = score*100
#             score = round(score,2)
#             # if score is not None:
#             #     st.text(f"Score: {score}%")

#         with col2:
#             st.text(recommended_movie_names[1])
#             st.image(recommended_movie_posters[1], use_column_width=True)
#             score = get_movie_score(recommended_movie_names[1], score_df)
#             score = score*100
#             score = round(score,2)
#             # if score is not None:
#             #     st.text(f"Score: {score}%")

#         with col3:
#             st.text(recommended_movie_names[2])
#             st.image(recommended_movie_posters[2], use_column_width=True)
#             score = get_movie_score(recommended_movie_names[2], score_df)
#             score = score*100
#             score = round(score,2)
#             if score is not None:
#                 st.text(f"Score: {score}%")



# if __name__ == "__main__":
#     Function_for_choose()
















