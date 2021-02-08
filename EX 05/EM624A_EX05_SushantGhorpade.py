# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 23:02:04 2020

@author: Sushant
"""
#-----------------------------part 1-----------------------------------#

import matplotlib.pyplot as plt

#----------------------------part 2 (Function)------------------------------------#
#define function get_index
def get_index(parts):
    if parts[1] == '1':                     #If 1 then return 'male'
        if parts[0] in ['1','2','3']:       #If 1,2,3 then male in low income range
            return 0
        elif parts[0] in ['4','5','6']:     #If 4,5,6 the male in mid income range
            return 1
        else:                               # If not in both then higher income range
            return 2
        
    else:                                   #If not 1 then 'female'
        if parts[0] in ['1','2','3']:       #If 1,2,3 then male in low income range
            return 3
        elif parts[0] in ['4','5','6']:     #If 4,5,6 the male in mid income range  
            return 4
        else:                               # If not in both then higher income range 
            return 5            

#----------------------------part 3 (Main program)---------------------------------#
    
myfile = open('marketingdata.txt','r')  #opening file
data = myfile.readlines()

counts = [0,0,0,0,0,0] # Counts list with six elements initialized with zero

for line in data:
    if 'NA' not in line:
        parts = line.strip().split()
        index = get_index(parts)
        counts[index] +=1

Low_income_men = counts[0]
Low_income_female = counts[1]

Mid_income_men = counts[2]
Mid_income_female = counts[3]

High_income_men = counts[4]
High_income_female = counts[5]

Total_lower_income = counts[0] + counts[1] 
Total_middle_income = counts[2] + counts[3]
Total_high_income = counts[4] + counts[5]

#print Results

print('\nLower income males:',Low_income_men,'\t Low income females:',Low_income_female,'\t\t Total Lower income:',Total_lower_income,'\n')
print('Middle income males:',Mid_income_men,'\t Middle income females:',Mid_income_female,'\t Total middle income:',Total_middle_income,'\n')
print('Upper income males:',High_income_men,'\t Upper income females:',High_income_female,'\t Total upper income:',Total_high_income,'\n')
#---------------------------------Visualization--------------------------------#

names = ['Low_income_men','Low_income_female','Mid_income_men','Mid_income_female','High_income_men','High_income_female']

#---------------------------------Bar plot---------------------------------------#
plt.figure(figsize=(10,7))
plt.subplot(221)
x = [0,1,2,3,4,5]
y = names
plt.bar(x,counts)
plt.title('Income wise classification using Bar Graph')
plt.xticks(x,names,rotation = 90)
plt.xlabel("Income Class")
plt.ylabel("Counts")
plt.tight_layout()

#------------------------------------Pie Plot-----------------------------------#
pie = [Total_lower_income,Total_middle_income,Total_high_income]

Wedges = ['Total lower income','Total middle income','Total upper income']

#Calculate percentage
Total = float(Total_lower_income + Total_middle_income + Total_high_income)
percent_low = round((1-Total_lower_income/Total)*100,2)
percent_mid = round((1-Total_middle_income/Total)*100,2)
percent_high = round((1-Total_high_income/Total)*100,2)

size = [percent_low,percent_mid,percent_high]

plt.subplot(222)
plt.pie(pie,labels= Wedges,autopct='%1.1f%%')
plt.title("Total Income Wise Distribution using Pie Chart")
plt.tight_layout()
plt.show()