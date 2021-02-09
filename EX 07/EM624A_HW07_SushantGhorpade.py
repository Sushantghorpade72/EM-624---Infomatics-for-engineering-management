# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:57:51 2020

@author: Sushant
"""
#Import packages
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Create list of stopwords
stopwords_file = open('stopwords_en.txt','r')

stopwords = []

for words in stopwords_file:
    words = words.rstrip('\n')
    stopwords.append(words)
    
#Import text files
pro_marijuana_file = open('pro_ marijuana_raw.txt','r')
con_marijuana_file = open('con_ marijuana_raw.txt','r')

#lowere alphabets and replace '\n' by spaces
pro_marijuana = pro_marijuana_file.read().lower().replace('\n','')
con_marijuana = con_marijuana_file.read().lower().replace('\n','')

#Remove digits
pro_data_nums = ''.join([text for text in pro_marijuana if text not in string.digits])
con_data_nums = ''.join([text for text in con_marijuana if text not in string.digits])

#Remove puncutation 
pro_data_punct = ''.join([text for text in pro_data_nums if text not in string.punctuation])
con_data_punct = ''.join([text for text in con_data_nums if text not in string.punctuation])

#tokenize text using nltk text tokenizer
pro_tokens = nltk.word_tokenize(pro_data_punct)
con_tokens = nltk.word_tokenize(con_data_punct)

#Remove words with character less that 3
pro_clean_tokens = [word for word in pro_tokens if len(word) > 3]
con_clean_tokens = [word for word in con_tokens if len(word) > 3]

#Remove stopwords
pro_clean_stopwords = [word for word in pro_data_punct if word not in stopwords]
con_clean_stopwords = [word for word in con_data_punct if word not in stopwords]

#Obviously frequent words
pro_common_words = nltk.FreqDist(pro_clean_tokens).most_common(10)
print ('\n---The 10 most frequent words in pro_ marijuana_raw.txt are:\n')
print (pro_common_words)

#Obviously frequent words
con_common_words = nltk.FreqDist(con_clean_tokens).most_common(10)
print ('\n---The 10 most frequent words in con_ marijuana_raw.txt are:\n')
print (con_common_words)

#We found frequent words that are related to marijuana are marijuana,use,legalization,drug,cannabis,legal,colorado,alcohol
#we shall add these to our list of stopwords
stopwords.extend(('marijuana','use','legalization','drug','cannabis','legal','alcohol','that'))

pro_clean_corpus = [word for word in pro_clean_tokens if word not in stopwords]
#print(nltk.FreqDist(pro_clean_corpus).most_common(10))
con_clean_corpus = [word for word in con_clean_tokens if word not in stopwords]
#print('\n',nltk.FreqDist(con_clean_corpus).most_common(10))

#calculating the sentiment using vader library
analyzer = SentimentIntensityAnalyzer()

#Vader analysis for pos_marijuana_raw.txt
pro_text_str = ' '.join(pro_clean_corpus)
pro_vad_sentiment = analyzer.polarity_scores(pro_text_str)

pro_pos = pro_vad_sentiment ['pos']
pro_neg = pro_vad_sentiment ['neg']
pro_neu = pro_vad_sentiment ['neu']

print ('\nThe following is the distribution of the sentiment for the file -', pro_marijuana_file)
print ('\n--- It is positive for', '{:.1%}'.format(pro_pos))
print ('\n--- It is negative for', '{:.1%}'.format(pro_neg))
print ('\n--- It is neutral for', '{:.1%}'.format(pro_neu), '\n')

#Vader analysis for con_marijuana_raw.txt
con_text_str = ' '.join(con_clean_corpus)
con_vad_sentiment = analyzer.polarity_scores(con_text_str)

con_pos = con_vad_sentiment ['pos']
con_neg = con_vad_sentiment ['neg']
con_neu = con_vad_sentiment ['neu']

print ('\nThe following is the distribution of the sentiment for the file -', con_marijuana_file)
print ('\n--- It is positive for', '{:.1%}'.format(con_pos))
print ('\n--- It is negative for', '{:.1%}'.format(con_neg))
print ('\n--- It is neutral for', '{:.1%}'.format(con_neu), '\n')

#Extracting Bigrams 
pro_Bigram = list(nltk.bigrams(pro_clean_corpus))
print ('\n------The following are the bigrams extracted from pro_ marijuana_raw.txt :')
print ('\n------Printing first 10 Bigrams\n',pro_Bigram[:10])
print ('\n------Total Bigrams in Pro marijuana files are',len(pro_Bigram))

con_Bigram = list(nltk.bigrams(con_clean_corpus))
print ('\n------The following are the bigrams extracted from con_ marijuana_raw.txt :')
print ('\n------Printing first 10 Bigrams\n',con_Bigram[:10])
print ('\n------Total Bigrams in Con marijuana files are',len(con_Bigram))

#Attach the bigrams to the list of words for the 2 texts
#We can use .extend to append Bigrams into our previous list but it will change the shape of the list
pro_final_list = []
con_final_list = []

for i in pro_clean_corpus:
    pro_final_list.append(i)

for j in pro_Bigram:
    pro_final_list.append(j)
    
for x in con_clean_corpus:
    con_final_list.append(x)
    
for y in con_Bigram:
    con_final_list.append(y)

print('\n-------There are',len(pro_clean_corpus),'objects in our pros list and',len(pro_Bigram),'in our bigrams list and we have a total of',len(pro_final_list),'objects')       
print('\n-------There are',len(con_clean_corpus),'objects in our cons list and',len(con_Bigram),'in our bigrams list and we have a total of',len(con_final_list),'objects')

#Creating wordcloud for Pro_Marijuanan
# Defining the wordcloud parameters
plt.figure(figsize=(12,9))
wc = WordCloud(background_color="white", max_words=200)
# Generate word cloud
wc.generate(pro_text_str)
# Store to file
wc.to_file('pro_cloud.png')
# Show the cloud
plt.title("WordCloud on Pro's of Marijuana")
plt.imshow(wc)
plt.axis('off')
plt.show()

#Creating wordcloud for Con_Marijuanan
# Defining the wordcloud parameters
plt.figure(figsize=(12,9))
wc = WordCloud(background_color="black", max_words=200)
# Generate word cloud
wc.generate(con_text_str)
# Store to file
wc.to_file('con_cloud.png')
# Show the cloud
plt.title("WordCloud on Con's of Marijuana")
plt.imshow(wc)
plt.axis('off')
plt.show()
