""" Write a Python program to print the Noun form of words in a sentence. Print both the word and its corresponding part-of-speech tag (POS) tagging.  """


from textblob import TextBlob
import pandas as pd

#import nltk
#import nltk.download("all")

sentence = input("Enter a Sentence : ")
blob = TextBlob(sentence)
noun =  [noun[0] for noun in blob.tags if noun[1]=="NN"]
print("Noun Form Words: ",noun)
for word , tag in blob.tags:
    print(word, " --------  " , tag)
