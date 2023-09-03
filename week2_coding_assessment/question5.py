""" Calculate the TF-IDF values for the words in a corpus using the TfidfVectorizer class and displays the resulting sparse matrix representation. Also, print the feature names and their corresponding indices. """

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
Tfidf = TfidfVectorizer()
corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]
values=Tfidf.fit_transform(corpus)
documents = ["Document "+str(i) for i in range(1,len(corpus)+1)]
features = Tfidf.get_feature_names()
for doc in corpus:
    for index,word in enumerate(doc.split(" ")):
          if word in features:
                print(word,"---: ",index)
    print("----------------")
pd.DataFrame(values.toarray(),columns=features,index=documents)
