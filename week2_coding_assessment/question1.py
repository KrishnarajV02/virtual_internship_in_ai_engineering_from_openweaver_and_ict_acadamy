""" In this week’s training, we discussed how a Fake News Detector Engine can be built. Apply sentiment analysis to capture the emotional tone of an article. Fake news might use extreme language or elicit strong emotional responses. Use NLTK’s VADER Sentiment Analyser or TextBlob’s Sentiment Analysis module on the dataset present in the kit. """


from textblob import TextBlob
import pandas as pd
fakenews = pd.read_csv("fakenews.csv") 
for i in range(len(fakenews)):
  blob = TextBlob (fakenews.iloc[i,0])
  sentiment_score = blob.sentiment.polarity
  if sentiment_score>0.25:
    sentiment = "Positive"
  elif sentiment_score <-0.25:
    sentiment = "Negative"
  else:
    sentiment = "Neutral"
  print(fakenews.iloc[i,0][:100] + "...", " ",sentiment)
  print("-"*120)
