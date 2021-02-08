#Currency exchange programme

#Inputs:
#How many Us Dollars you want to exchange ?
#Enter name of currency you want to convert into dollar ?
#What is the exchange rate ?

while True:
    user_input1 = input('Enter amount in dollars you want to exchange or type "done" to terminate: ')
    if user_input1 == 'done':
        break
    #Check if input 1 is digit value:
    if user_input1.isdigit() != True:
        print('Invalid input:"Integer value only!"')
        break
    else:
        user_input2 = str(input('Enter name of currency you want to convert into dollars: '))
        user_input3 = input('Enter exchange rate: ')
    
    #Check if input 3 is digit value:    
    if user_input3.isdigit() != True:
        print('Invalid input:"Integer value only!"')
        break
    else:
    #Print your answere:
         print('\n''You converted'+' '+user_input1+' '+'Dollar to'+' '+str(int(user_input1)*int(user_input3))+' '+user_input2)



    
