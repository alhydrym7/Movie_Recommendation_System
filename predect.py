import pandas as pd
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
cv_transforms = pickle.load(open('cv-transforms.pkl', 'rb'))

# Load the Multinomial Naive Bayes model
nb_classifier = pickle.load(open('movie-genre-mnb-model.pkl', 'rb'))

# Load the Random Forest model
rf_classifier = pickle.load(open('movie-genre-rfc-model.pkl', 'rb'))



data = pd.read_csv(r"C:\Users\asus\Downloads\movie_recommender_system-main\movie_recommender_system-main\dataset.csv")
unique_titles = data['genre'].drop_duplicates()
genres_for_maping=[]
# طباعة العناوين الفريدة بدون تكرار
for title in unique_titles:
    genres_for_maping.append(title)


from sklearn.preprocessing import LabelEncoder

# قم بإنشاء قائمة 'genres_for_maping' كما هو مبين في السؤال السابق

# قم بإنشاء نموذج LabelEncoder
label_encoder = LabelEncoder()

# قم بتطبيق النموذج على 'genres_for_maping' للحصول على القيم الرقمية
genres_numerical = label_encoder.fit_transform(genres_for_maping)

# قم بإنشاء قاموس لتخزين الأزواج النمطية (العناوين والقيم الرقمية)
genre_mapping_dict = {}

# استخدم حلقة for لإضافة الأزواج النمطية إلى القاموس
for genre, numerical_value in zip(genres_for_maping, genres_numerical):
    genre_mapping_dict[genre] = numerical_value

# Inverting the genre_mapping_dict (Swapping keys and values)
inverted_genre_mapping_dict = {v: k for k, v in genre_mapping_dict.items()}

# Now, genre_mapping_dict has numerical values as keys and genres as values.
genre_mapping_dict = inverted_genre_mapping_dict








# Function for preprocessing the text
def preprocess_text(dialog):
    ps = PorterStemmer()
    dialog = re.sub(pattern='[^a-zA-Z]', repl=' ', string=dialog)
    dialog = dialog.lower()
    words = dialog.split()
    dialog_words = [word for word in words if word not in set(stopwords.words('english'))]
    words = [ps.stem(word) for word in dialog_words]
    dialog = ' '.join(words)
    return dialog

# Function to predict movie genre using Naive Bayes model
def predict_genre_nb(dialog):
    preprocessed_dialog = preprocess_text(dialog)
    vectorized_dialog = cv_transforms.transform([preprocessed_dialog])
    genre_prediction_nb = nb_classifier.predict(vectorized_dialog)[0]
    genre_name_nb = genre_mapping_dict[genre_prediction_nb]

    return genre_name_nb

# Function to predict movie genre using Random Forest model
def predict_genre_rf(dialog):
    preprocessed_dialog = preprocess_text(dialog)
    vectorized_dialog = cv_transforms.transform([preprocessed_dialog])
    genre_prediction_rf = rf_classifier.predict(vectorized_dialog)[0]
    genre_name_rf = genre_mapping_dict[genre_prediction_rf]

    return genre_name_rf

# Example usage:
dialog_example = "A thrilling action-packed adventure in outer space."
predicted_genre_nb = predict_genre_nb(dialog_example)
predicted_genre_rf = predict_genre_rf(dialog_example)

print(f"Predicted genre using Naive Bayes: {predicted_genre_nb}")
print(f"Predicted genre using Random Forest: {predicted_genre_rf}")
