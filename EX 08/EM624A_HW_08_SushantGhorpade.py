# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:07:04 2020

@author: Sushant
"""
#Import Required Packages
import bs4 as bs
import requests
import nltk
import string
import re
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

body = requests.get('https://www.nytimes.com')
soup = bs.BeautifulSoup(body.content,'html.parser')

# Extract the plain text content from paragraphs
data = [paragraph.text.lower() for paragraph in soup.find_all('p')]

datalines = []
for lines in data:
    l = lines +'\n'
    datalines.append(l)

#Using pandas create a DataFrame
df = pd.DataFrame(datalines,columns=(['Content']))
 
#Function removes punctutation,digits and removes '\n'pattern
def cleaner(text):
    clean_text = "".join([word.replace('\n','') for word in text if word not in string.punctuation and word not in string.digits])
    return clean_text

#Apply function to all rows
df['clean_content'] = df['Content'].apply(lambda x: cleaner(x))
 
#Create tokenize words
def tokenize(text):
    tokens = re.split('\W+', text)
    return tokens

#Apply function to each row
df['clean_content'] = df['clean_content'].apply(lambda x: tokenize(x))
 
#Import given stopwords
stopwords_file = open('stopwords_en.txt','r')    
stop1 = [words.replace('\n', '') for words in stopwords_file]

# working with stopwords in NLTK
stop2 = list(nltk.corpus.stopwords.words('english'))

#Add both list
stop = stop1 + stop2

#Keep only unique values
stopwords = set(stop)

#Remove Stopwords
def Remove_Stopwords(token_list):
    clean_words = " ".join([word for word in token_list if word not in stopwords])
    return clean_words

df['clean_content'] = df['clean_content'].apply(lambda x: Remove_Stopwords(x))
 
# calculating the sentiment using vader library
analyzer = SentimentIntensityAnalyzer()

df['scores'] = df['clean_content'].apply(lambda x: analyzer.polarity_scores(x))

pd.set_option('display.max_columns', None)

#Create seprate columns for ach 
df['positive score'] = df['scores'].apply(lambda d:d['pos'])
df['negative score'] = df['scores'].apply(lambda d:d['neg'])
df['neutral score'] = df['scores'].apply(lambda d:d['neu'])

del df['scores'] #we don't need since we have specific column for each
#print(df.head())

#print the headlines with the highest and lowest sentiment for each
#for positive sentiments
print('\n--->Line with highest positive sentiment:\n',df.nlargest(3,'positive score'))
print('\n--->Line with lowest positive sentiment:\n',df.nsmallest(3,'positive score'))

#for negative sentiments
print('\n--->Line with highest negative sentiment:\n',df.nlargest(3,'negative score'))
print('\n--->Line with lowest negative sentiment:\n',df.nsmallest(3,'negative score'))

#for neutral sentiments
print('\n--->Line with highest neutral sentiment:\n',df.nlargest(3,'neutral score'))
print('\n--->Line with lowest neutral sentiment:\n',df.nsmallest(3,'neutral score'))


sentences = []

for elements in df['clean_content']:
        sentences.append(elements.split())
#print(sentences)        

texts = []

for text in sentences:
    for word in text:
        texts.append(word)        
#print(texts)

# calculate and print bigrams
bigrammed = list(nltk.bigrams(texts))
print('\n--->First 10 Bigrams\n',bigrammed[:11])

bi_list = []
for text in bigrammed:
    word = '_'.join(text)
    bi_list.append(word)
#print(bi_list)

#Merge into single list
all_words = []

for words in texts:
    all_words.append(words)

for pairs in bi_list:
    all_words.append(pairs)
    
print('\n--->Total objects in our "texts" list are',len(texts))
print('\n--->Total objects in our "bigram" list are',len(bi_list))
print('\n--->Sum of both list are',len(all_words))

#Creating wordcloud for above analysis
all_words_string = ' '.join(all_words)
# Defining the wordcloud parameters
plt.figure(figsize=(12,9))
wc = WordCloud(background_color="white", max_words=200)
# Generate word cloud
wc.generate(all_words_string)
# Store to file
#wc.to_file('cloud.png')
# Show the cloud
plt.title("WordCloud on New York Times")
plt.imshow(wc)
plt.axis('off')
plt.show()