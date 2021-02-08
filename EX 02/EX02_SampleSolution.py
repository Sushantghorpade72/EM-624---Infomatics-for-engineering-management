#Author: xyz
#Date: Today
# exercise 2 - sample solution

# We want to take an input (a number of cents, multiple of 5) and output the same amount

while True:

	cents = input("Please enter a number of cents (a multiple of 5) or 'done' to quit: ")

	#Do they want to quit?
	if cents == "done": break #if you have a very simple conditional, it can be on one line

	#Is the input a number?
	try:
		cents = int(cents)
	except:
		print ("Your input was not a valid number of cents. Pelase try again.\n")
		continue #start the loop over

	#Is it a multiple of 5?
	if cents % 5 != 0: # modulo operator tells you the remainder of the division
		print ("You did not enter a multiple of 5. Please try again.\n")
		continue #start the loop over

	#Is it a positive number?
	if cents <= 0:
		print ("Please enter a value greater than zero.\n")
		continue #start the loop over

	print ("You entered ", cents, " cents")

print ("\nGoodbye!")