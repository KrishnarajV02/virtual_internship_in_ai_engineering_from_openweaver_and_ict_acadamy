"""  In this week’s training, use POS tagging to extract information about the grammatical structure of the text. Fake news articles might have different distributions of POS tags compared to real news articles. """

from textblob import TextBlob
import pandas as pd
import nltk
nltk.download('all')

#output will be displayed at last after download completion

fakenews = pd.read_csv("fakenews.csv")
for i in range(len(fakenews)):
    blob = TextBlob(fakenews.iloc[i,0])
    if fakenews.iloc[i,1]==0:
        print("REAL")
        print("----")

    else:
        print("FAKE")
        print("----")
    tag = [tag[1] for tag in blob.tags]
    print(fakenews.iloc[i,0])
    print()
    print(" - ".join(tag))
    print("-"*120)
