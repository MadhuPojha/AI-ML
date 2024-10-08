import contractions
import re
from string import punctuation
import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
 
def clean_text(text):
    #remove contractions
    text = contractions.fix(text)
    #make lowercase
    text = text.lower()
    #remove punctuation
    text = re.sub('[%s]' % re.escape(punctuation), '', text)
    #remove numbers
    text = re.sub(r'\w*\d\w*', '', text)
    #remove stopwords
    stopwords = [stopword.strip() for stopword in open('./stopwords.txt', 'r')]
    return ' '.join([word for word in text.split() if word not in stopwords])
 
class Review:
    def __init__(self, review_text, score):
        self.review_text = review_text
        self.score = score
        self.cleaned_review_text = clean_text(review_text)
        self.sentiment = 'NEGATIVE' if score <= 2 else 'NEUTRAL' if score == 3 else 'POSITIVE'
 
 
#review1 = Review('Hello', 3.0)
#print(review1.sentiment)
 
reviews = []
try:
    with open('./Pet_Supplies_2000.json', 'r') as in_file:
        for line in in_file:
            try:
                data = json.loads(line)
                review_text = data['reviewText']
                overall = data['overall']
                reviews.append(Review(review_text, overall))
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line.strip()} - {e}")
except FileNotFoundError:
    print("The file pet_supplies.json was not found.")
    exit(1)
 
sentiments = {
    'NEGATIVE' : 0,
    'NEUTRAL' : 0,
    'POSITIVE' : 0
}
 
#for review in reviews:
#    sentiments[review.sentiment] += 1
#print(sentiments)
 
training_data, test_data = train_test_split(reviews, test_size= 0.2, random_state = 42)
train_x = [review.cleaned_review_text for review in training_data]
train_y = [review.sentiment for review in training_data]
 
test_x = [review.cleaned_review_text for review in test_data]
test_y = [review.sentiment for review in test_data]
 
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(train_x)
 
clf = SVC(kernel = 'linear')
clf.fit(vectors, train_y)
 
test_vectors = vectorizer.transform(test_x)
#print(clf.score(test_vectors, test_y))
 
for i, vector in enumerate(test_vectors):
    prediction = clf.predict(vector)
    if prediction[0] != test_y[i]:
        print(f'Predicted: {prediction[0]}')
        print(f'Was: {test_y[i]}')
 
print(clf.score(test_vectors, test_y))
