# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 03:23:34 2020

@author: Sushant
"""
# Importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import string
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# For scraping data from multiple pages
urls = []
review_list = []
critic = []
ratings = []

count = 0
for i in range(2,19):
    txt1 = 'https://www.rottentomatoes.com/m/ford_v_ferrari/reviews'
    txt2 = '?type=&sort=&page={0}'.format(i)
    # print(txt1+txt2)
    urls.append(txt1+txt2)
    count = count + i  
    
    j = 0
    while j < len(urls):
        NewUrl = urls[j]
        response = requests.get(NewUrl)
        soup = BeautifulSoup(response.text,'lxml')
        j = j + 1

    reviews = soup.find_all('div',attrs={'class':'the_review'})
    
    for i in range(0,len(reviews)):
        review_list.append(reviews[i].text.strip())
               
    authors = soup.find_all('a',attrs={'class':'unstyled bold articleLink'})
            
    for i in authors:
        critic.append(i.text)
        
    rating  = soup.find_all('div',attrs={'class':'small subtle review-link'})
    
    for i in rating:
        v = i.text.strip().replace('\r\n','')
        sc = v.split()[-1].replace('Review','NA')
        substring = '/'
        if substring in sc:
           sc = sc.split("/")[0]
           ratings.append(sc)

        else:
            if sc == 'A+':
                ratings.append(5)
            elif sc == 'A':
                ratings.append(4.8)
            elif sc == 'A-':
                ratings.append(4.6)
            elif sc == 'B+':
                ratings.append(4.45)
            elif sc == 'B':
                ratings.append(4.3)
            elif sc == 'B-':
                ratings.append(4.1)
            elif sc == 'C+':
                ratings.append(3.95)
            elif sc == 'C':
                ratings.append(3.8)
            elif sc == 'C-':
                ratings.append(3.6)
            elif sc == 'D+':
                ratings.append(3.45)
            elif sc == 'D':
                ratings.append(3.3)
            elif sc == 'D-':
                ratings.append(3.1)
            else:
                ratings.append("NA")
        
    
c1 = pd.DataFrame(critic,columns=['Critic Name'])   #convert Critic names column to dataframe
r1 = pd.DataFrame(review_list,columns=['Reviews'])  #convert reviews column to dataframe
s1 = pd.DataFrame(ratings,columns=['Score'])          #convert Scores column to dataframe

#pd.set_option('display.max_columns', None)
dataset = pd.concat([c1,r1,s1],axis = 1)            #Combine columns to single dataframe
dataset = dataset[dataset.Score != 'NA']
# print(dataset)
    
#Top 5 and botton reviews
dataset['Score'] = dataset['Score'].astype(float)
dataset = dataset[dataset.Score <= 5.0]
dataset = dataset.sort_values("Score",ascending = True)
# print(dataset.Score.unique())
top5 = dataset['Reviews'].tail(5)
bottom5 = dataset['Reviews'].head(5)
print('\n--->Top 5 reviews are:\n\n',top5)
print('\n--->Bottom 5 reviews are:\n\n',bottom5)

#Import stopwords
stopwords_file = open('stopwords_en.txt','r')

stopwords =[]

for stop in stopwords_file:
    words = stop.rstrip('\n')
    stopwords.append(words)

#Remove digits
review_top5_nums = ''.join([text for text in top5 if text not in string.digits])
review_bottom5_nums = ''.join([text for text in bottom5 if text not in string.digits])

#Remove puncutation 
review_top5_punct = ''.join([text.lower() for text in review_top5_nums if text not in string.punctuation])
review_bottom5_punct = ''.join([text.lower() for text in review_bottom5_nums if text not in string.punctuation])

#tokenize text using nltk text tokenizer
top5_tokens = nltk.word_tokenize(review_top5_punct)
bottom5_tokens = nltk.word_tokenize(review_bottom5_punct)

#Remove stopwords
top5_clean_stopwords = [word for word in top5_tokens if word not in stopwords]
bottom5_clean_stopwords = [word for word in bottom5_tokens if word not in stopwords]

review_str = ' '.join(top5_clean_stopwords)
#Defining the wordcloud parameters
plt.figure(figsize=(12,9))
wc = WordCloud(background_color="white", max_words=200)
# Generate word cloud
wc.generate(review_str)
# Store to file
wc.to_file('cloud_top5.png')
# Show the cloud
plt.title("WordCloud")
plt.imshow(wc)
plt.axis('off')
plt.show()

bottom5_str = ' '.join(bottom5_clean_stopwords)
#Defining the wordcloud parameters
plt.figure(figsize=(12,9))
wc = WordCloud(background_color="white", max_words=200)
# Generate word cloud
wc.generate(review_str)
# Store to file
wc.to_file('cloud_bottom5.png')
# Show the cloud
plt.title("WordCloud")
plt.imshow(wc)
plt.axis('off')
plt.show()    