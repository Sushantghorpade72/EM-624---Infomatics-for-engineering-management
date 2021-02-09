#EMx24 Ex08 Example Solution
#Author: ---
#Date: ---


# Importing required libraries
import urllib3
from bs4 import BeautifulSoup
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def txt_clean(word_str, min_len, stopwords_list):
    """
    Performs a basic cleaning to a list of words.

    :param word_str: string of words
    :type: string
    :param min_len: minimum length of a word to be acceptable
    :type: integer
    :param stopwords_list: list of stopwords
    :type: list
    :return: clean_words list of clean words
    :type: lists

    """
    clean_words = []
    word_list = word_str.split() #transforming the string of words into a list
    for word in word_list:
        word_l = word.lower().strip()
        if word_l.isalpha():
            if len(word_l) > min_len:
                if word_l not in stopwords_list:
                    clean_words.append(word_l)
                else:
                    continue
    return clean_words


# Connecting to the webpage and parsing the html file
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
url = 'http://www.nytimes.com/'

# getting the html of the current page
page = http.request('GET', url)

soup = BeautifulSoup(page.data, 'html.parser')

# Initializing the string to hold all the words in the headlines
headlines_words = ''

print ('\n--- Printing the headlines...')

for paragraph in soup.find_all('p'):
    text = paragraph.text
    print(text, '\n')
    headlines_words += ' '+ text

# Initializing a list for the stopwords
stopwords = []

# Creating a list of stopwords from text file
stopwordsfile = open('stopwords_en.txt','r')
for line in stopwordsfile:
    stopwords.append(line.strip())

# Adding words not relevant for this analysis to the stopwords list
stopwords.extend(('', 'trump', 'new', 'good', 'make', 'just', 'home', 'pm', 'et'))

min_len = 2 #setting the minimum lenght for the words

# cleaning the words
filtered_words = txt_clean(headlines_words, min_len, stopwords)

print ('\n--- Extracting bigrams from the text...')

# Extracting the bigrams
bigrams_list = [] # Initializing the list of bigrams
for i in range(len(filtered_words)):
    try:
        bigrams_list.append( filtered_words[i] + "_" + filtered_words[i+1] )
    except:
        pass # reached end of list

# Extracting the 7 most common bigrams, with their occurrence
common_bigrams_tuples = Counter(bigrams_list).most_common(7)

# Creating a list of the 7 most common bigrams (with no occurrences).
#   To keep the ouccurrence of the bigrams, each one is multiplied by its own occurrence.
#   This is relevant to give them the proper exposure in the wordcloud
common_bigrams = []
for bigram_tuple_count in range (0, len(common_bigrams_tuples)):
    multiple_bigram = (common_bigrams_tuples[bigram_tuple_count][0] + ' ') * int(common_bigrams_tuples[bigram_tuple_count][1])
    common_bigrams.append(multiple_bigram)

# Appending the list of most common bigrams to the list of words, generating the list for the wordcloud
#   and then transforming the list into a string
filtered_words.extend(common_bigrams)
wordcloud_str = ' '.join(filtered_words)

print ('\n--- Generating the wordcloud from the text...')

# Generating Wordcloud and its file

wc = WordCloud(background_color="white", max_words=4000)
wc.generate(wordcloud_str)
wc.to_file('NYT.png')

# Showing the cloud
plt.imshow(wc)
plt.axis('off')
plt.show()

print ('\n--- Calculating the sentiment for the text...')

# calculating the sentiment using vader library
analyzer = SentimentIntensityAnalyzer()
vad_sentiment = analyzer.polarity_scores(wordcloud_str)

pos = vad_sentiment ['pos']
neg = vad_sentiment ['neg']
neu = vad_sentiment ['neu']

print ('\nThe following is the distribution of the sentiment')
print ('\n--- It is positive for', '{:.1%}'.format(pos))
print ('\n--- It is negative for', '{:.1%}'.format(neg))
print ('\n--- It is neutral for', '{:.1%}'.format(neu), '\n')



print ('\n--- END OF PROCESSING ---\n')
