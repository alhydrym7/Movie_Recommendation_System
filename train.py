# Importing essential libraries
import pandas as pd
import pickle

# Loading the dataset
df = pd.read_csv(r"C:\Users\asus\Downloads\movie_recommender_system-main\movie_recommender_system-main\dataset.csv")
df['overview'] = df['overview'].astype(str)

unique_titles = df['genre'].drop_duplicates()
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

# # Mapping the genres to values
# genre_mapper = {'other': 0, 'action': 1, 'adventure': 2, 'comedy':3, 'drama':4, 'horror':5, 'romance':6, 'sci-fi':7, 'thriller': 8}
df['genre'] = df['genre'].map(genre_mapping_dict)

# Removing the 'id' column
df.drop('id', axis=1, inplace=True)

# Importing essential libraries for performing Natural Language Processing on given dataset
import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Cleaning the text
corpus = []
ps = PorterStemmer()

for i in range(0, df.shape[0]):

  # Cleaning special character from the dialog/script
  dialog = re.sub(pattern='[^a-zA-Z]', repl=' ', string=df['overview'][i])

  # Converting the entire dialog/script into lower case
  dialog = dialog.lower()

  # Tokenizing the dialog/script by words
  words = dialog.split()

  # Removing the stop words
  dialog_words = [word for word in words if word not in set(stopwords.words('english'))]

  # Stemming the words
  words = [ps.stem(word) for word in dialog_words]

  # Joining the stemmed words
  dialog = ' '.join(words)

  # Creating a corpus
  corpus.append(dialog)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=10000, ngram_range=(1,2))
X = cv.fit_transform(corpus).toarray()
y = df['genre'].values
print(y)

# Creating a pickle file for the CountVectorizer
pickle.dump(cv, open('cv-transforms.pkl', 'wb'))

# Model Building

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import MultinomialNB
nb_classifier = MultinomialNB(alpha=0.1)
nb_classifier.fit(X_train, y_train)

# Creating a pickle file for the Multinomial Naive Bayes model
filename = 'movie-genre-mnb-model.pkl'
pickle.dump(nb_classifier, open(filename, 'wb'))

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=7)
rf.fit(X_train, y_train)
#ypred=rf.predict(X_test)


filename1 = 'movie-genre-rfc-model.pkl'
pickle.dump(rf, open(filename1, 'wb'))
    







