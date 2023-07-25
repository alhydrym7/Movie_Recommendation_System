import streamlit as st
from PIL import Image
import pandas as pd
import requests
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer
import nltk
nltk.download('stopwords')

# Load the CountVectorizer model
cv_transforms = pickle.load(open(r'C:\Users\asus\Desktop\Artificial intelligence\Third Year\Summer\EVC\Dataanlysez\cv-transforms.pkl', 'rb'))

# Load the Multinomial Naive Bayes model
nb_classifier = pickle.load(open(r'C:\Users\asus\Desktop\Artificial intelligence\Third Year\Summer\EVC\Dataanlysez\movie-genre-mnb-model.pkl', 'rb'))

# Load the Random Forest model
rf_classifier = pickle.load(open(r'C:\Users\asus\Desktop\Artificial intelligence\Third Year\Summer\EVC\Dataanlysez\movie-genre-rfc-model.pkl', 'rb'))

data = pd.read_csv(r"C:\Users\asus\Downloads\movie_recommender_system-main\movie_recommender_system-main\dataset.csv")
unique_titles = data['genre'].drop_duplicates()
genres_for_maping = []

for title in unique_titles:
    genres_for_maping.append(title)

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
genres_numerical = label_encoder.fit_transform(genres_for_maping)
genre_mapping_dict = {}

for genre, numerical_value in zip(genres_for_maping, genres_numerical):
    genre_mapping_dict[genre] = numerical_value

inverted_genre_mapping_dict = {v: k for k, v in genre_mapping_dict.items()}
genre_mapping_dict = inverted_genre_mapping_dict

def preprocess_text(dialog):
    ps = PorterStemmer()
    dialog = re.sub(pattern='[^a-zA-Z]', repl=' ', string=dialog)
    dialog = dialog.lower()
    words = dialog.split()
    dialog_words = [word for word in words if word not in set(stopwords.words('english'))]
    words = [ps.stem(word) for word in dialog_words]
    dialog = ' '.join(words)
    return dialog

def predict_genre_nb(dialog):
    preprocessed_dialog = preprocess_text(dialog)
    vectorized_dialog = cv_transforms.transform([preprocessed_dialog])
    genre_prediction_nb = nb_classifier.predict(vectorized_dialog)[0]
    genre_name_nb = genre_mapping_dict[genre_prediction_nb]

    return genre_name_nb

def predict_genre_rf(dialog):
    preprocessed_dialog = preprocess_text(dialog)
    vectorized_dialog = cv_transforms.transform([preprocessed_dialog])
    genre_prediction_rf = rf_classifier.predict(vectorized_dialog)[0]
    genre_name_rf = genre_mapping_dict[genre_prediction_rf]

    return genre_name_rf

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

page = st.sidebar.selectbox("كيف ترغب في البحث؟", ["الصفحة الرئيسية", "عن طريق التشابه", "عن طريق المعلومات","عن طريق وصف للفيلم"])

if page == "الصفحة الرئيسية":
    st.header('مرحبًا بك في نظام توصية الأفلام')
    st.write("<span style='font-family: Arial; color: #C4CA02; font-size: 45px;'>تم التصميم بواسطة: </span>", unsafe_allow_html=True)
    st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>1. محمد عادل</span>", unsafe_allow_html=True)
    st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>2. عبدالرحمن خالد </span>", unsafe_allow_html=True)
    st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>3. شهد محمد </span>", unsafe_allow_html=True)
    st.write("<span style='font-family: Arial; color: #94E6E6; font-size: 25px;'>4. إكرام فراس </span>", unsafe_allow_html=True)
    st.write("<span style='font-family: Arial; color: #C4CA02; font-size: 35px;'>هذا المشروع تحت إشراف:</span>", unsafe_allow_html=True)
    st.write("<span style='text-align: center: Arial; color: #94E6E6; font-size: 20px;'>1. المهندسه مروى </span>", unsafe_allow_html=True)
    st.write("<span style='text-align: center: Arial; color: #94E6E6; font-size: 20px;'>2. المهندس إبراهيم</span>", unsafe_allow_html=True)

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

elif page == "عن طريق المعلومات":
    st.header("معلومات الفيلم")

    program = pd.read_pickle("program.pkl")

    quality_options = ["SD", "HD"]
    quality = st.selectbox("أدخل جودة الفيلم:", quality_options)
    
    genre2 = program["genre"].unique()
    genre = st.selectbox("أدخل التصنيف المطلوب:", genre2)

    film_or_series_options = ["فلم", "مسلسل"]
    film_or_series = st.selectbox("هل تبحث عن فلم أم مسلسل:", film_or_series_options)

    num = st.slider("اختر عدد التوصيات التي تريدها:", min_value=1, max_value=10, step=1, value=5)
    
    if st.button("البحث"):
        quality_value = 1 if quality == "HD" else 0
        film_or_series = "movie" if film_or_series == "فلم" else "series"
        filtered_data = program[
            (program["genre"] == genre) &
            (program["type"] == film_or_series) &
            (program["hd"] == quality_value)
        ]
        filtered_data = filtered_data.sort_values(by='number_of_watches', ascending=False)
        filtered_data = filtered_data[["type", "genre", "name", "number_of_watches"]]

        # تطبيق التنسيق على DataFrame باستخدام applymap
        styled_data = filtered_data.head(num).style.set_table_attributes('style="text-align: center"')

        # عرض الجدول المُنسق
        st.table(styled_data)


elif page == "عن طريق وصف للفيلم":
    st.header("وصف الفلم")
    video_description = st.text_area("اكتب وصفًا للفيلم هنا:")
    if st.button("التنبؤ بالتصنيف"):
        predicted_genre_nb = predict_genre_nb(video_description)
        predicted_genre_rf = predict_genre_rf(video_description)

        # st.write(f"التصنيف المتوقع باستخدام نموذج Naive Bayes: {predicted_genre_nb}")
        st.write(f" Random Forest التصنيف المتوقع باستخدام:=======>>     {predicted_genre_rf}")

# Add CSS styles to ensure right-to-left text alignment
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
