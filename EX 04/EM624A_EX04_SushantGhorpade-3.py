# -*- coding: utf-8 -*-
"""
@author: Sushant
"""
import os
os.getcwd()
#open citi bike file
file = open('citi_bike.txt','r')

# create empty list
data = []


for line in file:
    parts = line.strip().split()
    data.append(parts)

#pass list inside function

def print_details(List):

    #Empty lists to append data to each specific month
    
    january = []
    february = []
    march = []
    april = []
    may = []
    june = []
    july = []  
    august = []
    september =[]
    october = []
    november = []
    december = []

#write a for loop to execute it
    for parts in List:
        if parts[0].startswith("1"):
            january.append(parts)
        elif parts[0].startswith("2"):
            february.append(parts)
        elif parts[0].startswith("3"):
            march.append(parts)
        elif parts[0].startswith("4"):
            april.append(parts)
        elif parts[0].startswith("5"):
            may.append(parts)            
        elif parts[0].startswith("6"):
            june.append(parts)
        elif parts[0].startswith("7"):
            july.append(parts)
        elif parts[0].startswith("8"):
            august.append(parts)
        elif parts[0].startswith("9"):
            september.append(parts)
        elif parts[0].startswith("10"):
            october.append(parts)
        elif parts[0].startswith("11"):
            november.append(parts)
        elif parts[0].startswith("12"):
            december.append(parts)


#a.	Loop through each list of your list of lists to calculate the average daily miles traveled and total 24-­hour pass purchases for that month

    total_passes = 0
    total_miles = 0
    
    
    if len(january) > 0:
        for i in january:
            total_passes = int(total_passes) + int(i[7])
            total_miles = float(total_miles) + float(i[3])       
        print('Total 24-­hour pass purchases for month of January',total_passes)
        print('Average miles per day for month of January',round(total_miles/len(january),2),'\n')
    
    if len(february) > 0:
        for i in february:
            total_passes = int(total_passes) + int(i[7])
            total_miles = float(total_miles) + float(i[3])       
        print('Total 24-­hour pass purchases for month of February',total_passes)
        print('Average miles per day for month of February',round(total_miles/len(february),2),'\n')
   
    if len(march) > 0:
        for i in march:
            total_passes = int(total_passes) + int(i[7])
            total_miles = float(total_miles) + float(i[3])       
        print('Total 24-­hour pass purchases for month of March',total_passes)
        print('Average miles per day for month of March',round(total_miles/len(march),2),'\n')
    
    if len(april) > 0:
        for i in april:
            total_passes = int(total_passes) + int(i[7])
            total_miles = float(total_miles) + float(i[3])       
        print('Total 24-­hour pass purchases for month of April',total_passes)
        print('Average miles per day for month of April',round(total_miles/len(april),2),'\n')
    if len(may) > 0:
        for i in may:
            total_passes = int(total_passes) + int(i[7])
            total_miles = float(total_miles) + float(i[3])       
        print('Total 24-­hour pass purchases for month of April',total_passes)
        print('Average miles per day for month of April',round(total_miles/len(may),2),'\n')

    if len(june) > 0:
        for i in june:
            total_passes = int(total_passes) + int(i[7])
            total_miles = float(total_miles) + float(i[3])       
        print('Total 24-­hour pass purchases for month of June',total_passes)
        print('Average miles per day for month of June',round(total_miles/len(june),2),'\n')

    if len(july) > 0:
        for i in july:
            total_passes = int(total_passes) + int(i[7])
            total_miles = float(total_miles) + float(i[3])       
        print('Total 24-­hour pass purchases for month of July',total_passes)
        print('Average miles per day for month of July',round(total_miles/len(july),2),'\n')

    if len(august) > 0:
        for i in august:
            total_passes = int(total_passes) + int(i[7])
            total_miles = float(total_miles) + float(i[3])       
        print('Total 24-­hour pass purchases for month of August',total_passes)
        print('Average miles per day for month of August',round(total_miles/len(august),2),'\n')

    if len(september) > 0:
        for i in september:
            total_passes = int(total_passes) + int(i[7])
            total_miles = float(total_miles) + float(i[3])       
        print('Total 24-­hour pass purchases for month of September',total_passes)
        print('Average miles per day for month of September',round(total_miles/len(september),2))

    if len(october) > 0:
        for i in october:
            total_passes = int(total_passes) + int(i[7])
            total_miles = float(total_miles) + float(i[3])       
        print('Total 24-­hour pass purchases for month of October',total_passes)
        print('Average miles per day for month of October',round(total_miles/len(october),2))
 
    if len(november) > 0:
        for i in november:
            total_passes = int(total_passes) + int(i[7])
            total_miles = float(total_miles) + float(i[3])       
        print('Total 24-­hour pass purchases for month of November',total_passes)
        print('Average miles per day for month of November',round(total_miles/len(november),2))

    if len(december) > 0:
        for i in december:  
            total_passes = int(total_passes) + int(i[7])
            total_miles = float(total_miles) + float(i[3])       
        print('Total 24-­hour pass purchases for month of December',total_passes)
        print('Average miles per day for month of December',round(total_miles/len(december),2))


#Print blank line
    print('\n')

#c.	Print the first and last day in your data using list indexes. 
    print('The following data is from',List[0][0],'to',List[-1][0],'\n')

#print blank line
    print('\n')

#e.	Print the average miles
#f.	Print the total number of pass purchased
    avg_miles = 0
    total_pass = 0

    for i in List:   
        avg_miles = float(avg_miles) + float(i[4])  
        total_pass = int(total_pass) + int(i[7]) + int(i[8])     
    print('Total pass purchased: ',total_pass)
    print('Average miles: ',round(total_miles/len(List),2),'\n')


#g.	Print top 5 days with higher number of trips (item 2).
    x = []
    top_dates = []
    for i in List:
        x.append(int(i[1]))
    
    x = sorted(x,reverse=True)

    x = x[0:5]
    #print(x)

    for i in List:
        if int(i[1]) in x:
            top_dates.append(i[0])
        
    print('top 5 days with higher number of trips are: ',top_dates)

    print('\n'"This is end of file processing"'\n')   

#--------------------------part 3------------------------------------#
#Read city bike csv
bike = open('citi_bike.csv','r')

# create empty list
citi_bike_data = []


for line in bike:
    parts = line.strip().split(',')
    citi_bike_data.append(parts)    
    
#--------------------------part 4------------------------------------#   
#Merge both csv and txt file into a pandas structure and print it    
final_data = []

for element in citi_bike_data:
    final_data.append(element)

for element in data:
    final_data.append(element)
    
    
print(final_data)

import pandas

dataframe = pandas.DataFrame(final_data)
dataframe.columns = ['Date','Trips over the past 24-hours (5 pm to 5 pm)','Cumulative trips (since launch)',
                     'Miles traveled today (5 pm to 5 pm)','Miles traveled to date','Total Annual Members','Annual Member Sign-Ups (5pm - 5pm)',
                     '24-Hour Passes Purchased (5 pm - 5 pm)','7-Day Passes Purchased (5 pm - 5 pm)']

pandas.set_option('display.max_columns', None)
print(dataframe)

    
