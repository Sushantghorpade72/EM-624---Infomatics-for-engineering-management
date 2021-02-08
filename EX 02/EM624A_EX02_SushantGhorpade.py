#Author: Sushant Ghorpade
#Description: 
# Write the program as a loop to prompt the user for input and print the input, until the user inputs ‘done’ (without quotes).
#The user should be prompted for a price in cents. They will enter the word ‘done’ (no quotes) to finish.
# Enter the price as cents, a multiple of five cents, or ‘done’ (without quotes) if you are finished
# The program is written as a loop (using while True), so that the user
#     must enter the word 'done" (without quotes) to signal
#     that they want to end

while True:
    currency_input = input('Enter your currency in cents(multiple of 5) or type "done" to terminate: ')
    #Condition 1:Check if user wants to terminate the code.
    if currency_input == 'done':
        print('\n''Thankyou for using the tool.Goodbye!''\n')
        break
    #Condition 2: Check if input is digit,ask for valid input again
    elif currency_input.isdigit() == False:
        print('\n''Sorry!Please enter valid number''\n')
        continue
    #Condition 3: Check if number is  multiple of 5 or ask for valid input again
    elif float(currency_input)%5 != 0:
        print('\n''Invalid input.Curreny not multiple of 5''\n')
        continue
    #Condition 4: If input satisfies both conditons, print final output
    else:
        currency_input.isdigit() == True and float(currency_input)%5 == 0
        print('\n''You entered',currency_input,'cents''\n')
        continue
    
           