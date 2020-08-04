# Importing the required modules
import NumberValidation as checker
import NumberSystemConversions as conversion
import BitAdder

# The main module 
def main_function():
	continuation=True
	# Using While Loop
	while continuation==True:
		number1=checker.validate(1)
		number2=checker.validate(2)
		# Converting the entered numbers to decimal by passing the function decimal_to_binary from NumberSystemConversions Module
		firstActualBinaryConversion=conversion.decimal_to_binary(number1)
		secondActualBinaryConversion=conversion.decimal_to_binary(number2)
		binary_sum=BitAdder.bit_add(firstActualBinaryConversion,secondActualBinaryConversion)
		# Printing the binarysum if it does not exceed 8 bit
		if len(str(binary_sum))<=8:
			print("\n----------------Result----------------")
			print("The Binary Sum of",number1,"and",number2,"is",binary_sum,"\n")
		else:
			# Error message showing the binary sum exits 8-bit
			print("\n-------------------------------------------------------------------")
			print("The Binary Sum exceeds 8 bit. Cannot be performed.Please try again.")
			print("-------------------------------------------------------------------")
			
		askingContinuation=True
		# Using While Loop
		while askingContinuation==True:		
			# Asking user if they want to continue 
			asking_user=input("\nDo want to enter again? (Y/N) ")
			# If conditions
			# Ending the program if the user enters "n" or "N" 
			if asking_user=="n" or asking_user=="N" : 
				print("\n-----------------------------------")
				print("Thank You for using the application")
				print("-----------------------------------")
				continuation=False
				break 
			# Exiting the current loop so that the user can enter numbers again if the user enters "y" or "Y" 
			elif asking_user=="y" or asking_user=="Y":
				break
			else:
				# Displaying error message if the entered value by the user is not valid
				print("Please enter Y or N only.\n")

# Calling the main_function() function								
main_function()
