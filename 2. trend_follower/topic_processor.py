# import nltk
from nltk.util import ngrams
import re
from tqdm import tqdm
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


class Corpus():
    def __init__(self, n_gram=2):
        self.wc = WordCloud(width=1200, height=900,
                            max_words=100,
                            #    background_color='white'
                            )
        self.n_gram = n_gram

    def n_gramize(self, acl):
        word_bag = []

        for i in tqdm(acl, desc='n_gramizing... '):

            symbol_deleted = re.sub(
                r"[^\uAC00-\uD7A30-9a-zA-Z\s]", " ", i.lower())

            # stopwords = nltk.corpus.stopwords.words('english')
            # stopwords.append('a')
            # stopwords_deleted = [i for i in symbol_deleted.split() if not i in stopwords]

            # word_bag.extend(ngrams(stopwords_deleted, n=2))

            word_bag.extend(ngrams(symbol_deleted.split(), n=self.n_gram))

        return word_bag

    def make_word_cloud(self, count_of_ngrams):
        cloud = self.wc.generate_from_frequencies(dict(zip([' '.join(
            i) for i in count_of_ngrams.value_counts().keys()], count_of_ngrams.value_counts().values)))
        plt.figure(figsize=(12,9))
        plt.axis('off')
        plt.imshow(cloud)
        plt.show()
        return cloud

    def make_wordcloud_with(self, word_list):
        ngram = self.n_gramize(word_list)
        return self.make_word_cloud(pd.Series(ngram))