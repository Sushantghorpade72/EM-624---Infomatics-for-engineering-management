
"""
@author: Sushant Ghorpade
"""
##PART 1:
#Open the file
myfile = open('marketingdata.txt','r')

#Read data from the file
data = myfile.readlines()

count_lines_no_na = 0
total_no_na = 0
with_na = 0

print('\n''For Part 1')
print('\n')
print('These are the first twenty lines in the file with no "NA" in it')

for i in data:
    i = i.rstrip("\n")
    if 'NA' not in i:
        total_no_na = total_no_na + 1
        if count_lines_no_na <= 19:
            count_lines_no_na = count_lines_no_na +1
            print(i)
    else:
        with_na = with_na +1
        
print('\n')
percent = round((with_na/len(data))*100,2)

print('The file has',total_no_na,'lines with no"NA" in it.The lines with "NA" are',percent,'% of the total lines''\n')


##PART 2:
#Open the file
bike_file = open('NYC-CitiBike-2016.csv','r')

#Read data from the file
data = bike_file.readlines()

total = 0
with_date = 0

print('\n')
# print("The file has n2 lines, of which n3 are from 9/29/16")
for i in data:
    total = total + 1
    i = i.rstrip("\n")
    if '9/29/16' in i:
        with_date = with_date + 1
        
#print(total)
#print(with_date)

percentage = round((with_date/total)*100,4)

#print(percentage)

print('\n''For Part 2''\n')
print('The file has',total,'of which',with_date,'are from 9/29/16''\n')


if total > with_date:
    print("The first file is larger than the second one"'\n')
else:
    print("The first file is smaller than the second one"'\n')

print('The file has',total,'of which',with_date,'are from 9/29/16.The lines from 9/29/16 are',percentage,'% of the total lines')