import contractions
import re
from string import punctuation

def clean_text(text):
    # remove contractions
    text = contractions.fix(text)

    # make lowercase
    text = text.lower()

    # remove punctuation
    text = re.sub('[%s]' % re.escape(punctuation), '', text)

    # remove numbers
    text = re.sub(r'\w*\d\w*', '', text)

    # remove stopwords
    stopwords = [stopword.strip()  for stopword in open('./data/stopwords.txt', 'r')]

    # return string
    return ' '.join([word for word in text.split() if word not in stopwords])
    

text = "I read this book for  the first time in 1987, and it's still one of my favorites!"
cleaned_text = clean_text(text)
print(cleaned_text)