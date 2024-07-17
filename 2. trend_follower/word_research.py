# https://wonhwa.tistory.com/23 불용어, 표제어

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
import pandas as pd

import crawler

def lemmatizer(sentences):
    # nltk.download('all')
    # nltk.download('wordnet')
    # nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.append('a')

    lemmatizer = WordNetLemmatizer()
    token = RegexpTokenizer('[\w]+')
    result_pre_lem = [token.tokenize(i) for i in sentences]
    # middle_pre_lem= [r for i in result_pre_lem for r in i]
    middle_pre_lem = []
    for i in result_pre_lem:
        for r in i:
            middle_pre_lem.append(r.lower())
    final_lem = [lemmatizer.lemmatize(i) for i in middle_pre_lem if not i in stopwords] # 표제어 추출 및 불용어 제거

    english = pd.Series(final_lem).value_counts()
    
    return english
