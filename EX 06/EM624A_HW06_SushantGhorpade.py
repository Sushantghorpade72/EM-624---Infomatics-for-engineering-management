# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:24:57 2020

@author: Sushant
"""

import pandas as pd

#import data using pandas

movies = pd.read_table('movies.dat',sep= '::',header=None,names= ('MovieID','Titles','Genres'))
rating = pd.read_table('ratings.dat',sep= '::',header=None,names= ('UserID','MovieID','Ratings','Timestamps'))
users = pd.read_table('users.dat',sep= '::',header=None,names= ('UserID','Gender','Age','Occupation','Zip-code'))

#---------------------------print first 3 rows of each DataFrame-------------------------#
print('\nFirst 3 rows form movies dataset:\n\n',movies.head(3),'\n')
print('\nFirst 3 rows form rating dataset:\n\n',rating.head(3),'\n')
print('\nFirst 3 rows form user dataset:\n\n',users.head(3),'\n')

#-------------Merging into single Data Frame---------------------------------------------#
df1 = movies.merge(rating,how= 'inner')
data = df1.merge(users,how='inner')
#data.info()

#-------------------print records for all 4 Data Frame---------------------------------------------#
print('\nRecords in "movies" dataset:',len(movies))
print('\nRecords in "rating" dataset:',len(rating))
print('\nRecords in "users" dataset:',len(users))
print('\nRecords in "data" dataset:',len(data))

#-------------------Replace values of occupation column---------------------------------------------#
occupation_dict = {0:'other/not specified',1:'academic/educator',2:'artist',3:'clerical/admin',4:'college/grad student',
                    5:'customer service',6:'doctor/health care',7:'executive/managerial',8:'farmer',9:'homemaker',10:'K-12 student',
                    11:'lawyer',12:'programmer',13:'retired',14:'sales/marketing',15:'scientist',16:'self-employed',
                    17:'technician/engineer',18:'tradesman/craftsman',19:'unemployed',20:'writer'}

data['Occupation'].replace(occupation_dict,inplace=True)

#------------------------------Last 3 rows of dataFrame---------------------------------------------#
print('\n\n\nLast 3 rows of "data" DataFrame:\n\n',data.tail(3),'\n')

#--------------------Find the 5 occupations that give higher ratings for movies on DataFrame -------#
top_5 = data.groupby(['Occupation']).count()
top_5 = top_5.sort_values(by='Ratings',ascending=False)
print('\n\n5 occupations that give higher ratings for movies:\n\n',top_5.head())