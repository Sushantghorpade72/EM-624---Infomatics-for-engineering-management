# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:05:02 2020

@author: Sushant
"""

#Section 2: Code Checking
#Q6.Write a script that takes a string as input from the user and 
#prints a string where for every character in the original, 
#there are three characters (example: 'The' → 'TTThhheee').

#Answer: The result of the code provided to us was not which was required.
#        Lets consider the above example. The output to the input was [T,h,e,T,h,e,T,h,e]
#        Hence, we modified code to get required ouput. We also provided a "done" condition 
#        incase we want to terminate the code   
#Modified Code
    
N = input("Enter your characters: ")
L = []
for letters in N:
     L.append(letters*3)
print(''.join(L))

#Q7.Write a script that calculates the 3 longest words of a text stored in a file and print them from the 
#longest to the smaller of the 3. Please note:
#The name of the file is word_list.csv and it doesn’t need to be asked to the user (meaning the 
#name will be in the code)
#Assume that the file contains n records, each one composed by 1 word. Words can be present 
#more than once, but only unique words need to be considered
#A sample word_list.csv file is attached for testing.

#modified code
handle = open('word_list.csv','r')
top3 = ["","",""]
for line in handle:
    #For each line in the file, strip the input and put it into the word variable
    word = line.strip()
    #Compare the length of each incoming word to the length of each word in each position
    for i in range(0,3):
        top3.sort(key = len) 
        if (len(word) > len(top3[i])):
            top3[i] = word
#Print the words
print ("\nThe 3 longest words are:", top3)


print('\nAnswer: The given code runs properly. The only change we need to do is shift the ",top3" inside parentheses\n')



#Q8.Write a script that takes a character (i.e. a string of length 1) as input from 
#the user and returns False if it is a consonant, True otherwise. 
#A check on the length of the input string and its being alphabetical is required 
#and if not, send a message to the user and ask again

#Modified code

while True:
    user_input = input('Please enter an single alphabetical character or "done" to terminate: ')
    if user_input == "done":
        print('Thank you')
        break
    else:
        if user_input.isdigit() == True:
            print('please enter an alphabet')
            break
            
        if len(user_input) > 1:
            print('please enter only single letter')
            break
        
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        
        if user_input in vowels:
            print(True)
        else:
            print(False)


        
#--------------------------------Section 3 code writing----------------------------########
print('\n#--------------------------------Section 3 code writing------------------------####\n')

import pandas as pd
import matplotlib.pyplot as plt
#####-------------------------------------Q9.Answer------------------------------##########
print('\n#####-------------------------------------Q9.Answer------------------------------###\n')


#import data
file1 = open('ai_trends.txt','r')
file2 = open('stopwords_en.txt','r')

#create empty list to append content later
data = []
stopwords = []

#Add elements to list of stopwords
for elements in file2:
    element = elements.replace('\n','')
    stopwords.append(element) 

#Creating list out of file    
for text in file1:
    content = text.lower().replace('\n','').split()
    data.append(content)
    
ai_trend = []

for objects in data:                # loop to itreate with sublist
    for element in objects:          #loop to iterate with items in sublist
        ai_trend.append(element)    
    
#Create list without stopwords using list comprehension
clean_data = [val for val in ai_trend if val not in stopwords]    
    
#create list of unique elements
unique_elements = list(set(clean_data))  

#Creating dictionary for word count  
dictionary = dict.fromkeys(unique_elements,0)

for i in dictionary:
    count = 0
    for j in clean_data:
        if i == j:
            count += 1
            
        dictionary[i] = count   

#a. Dictionary with occurance of word        
dictionary = {key: value for key,value in sorted(dictionary.items(), key=lambda item: item[1])}        
print(dictionary)    

#Creat a bar graph with 10 most frequent words.
df = pd.DataFrame.from_dict(dictionary, orient="index").reset_index()
df.columns = ['Word', 'Count']
df_1=df.sort_values('Count')
df_1= df_1.tail(10)      

plt.figure(figsize=(10,7))
plt.title('Frequency of top 10 words')
df_1.plot(x ='Word', y='Count', kind = 'bar')
    
#b.Calculate the longest word
list1 = []
list1 = df['Word'].tolist()
max_len = 1
for ele in list1: 
    if len(ele) > max_len: 
        max_len = len(ele) 
        res = ele
        
print('\n\n Longest word in list is:',res)        
        
#c.Average word length
ave_length = sum(len(e) for e in unique_elements)/len(unique_elements)
print('\n\n Average word length is: ',ave_length)




########-----------------------Q10.Answer----------------------------##########
print('\n########-----------------------Q10.Answer----------------------------##########\n')

cars = pd.read_csv('cars.csv')

#a.the first 3 rows and the last 3 of the dataset
print('First 3 rows:\n\n',cars.head(3),'\n')
print('\nLast 3 rows:\n\n',cars.tail(3))

#b.the 3 cars with the lowest average-mileage.
low = cars.nsmallest(3,['average-mileage'])
print('\n The 3 cars with lowest average-milage are given below: \n\n',low)

#c.the 3 cars with the highest average-mileage.
high = cars.nlargest(3,['average-mileage'])
print('\n The 3 cars with lowest average-milage are given below: \n\n',high)

