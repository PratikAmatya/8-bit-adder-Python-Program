# function which returns the correct number entered by the user
def validate(numberPosition):
	correctNumberEntered=False
	while correctNumberEntered == False:
		# Exception Handling using try except block
		try:
			if numberPosition==1:
				# Converting the entered number to Int datatype
				number=int(input("\nEnter the first number in decimal number system: "))
			else:
				number=int(input("\nEnter the second number in decimal number system: "))
			# Returning the number if it is in range
			if number >=0 and number <256:
				return number
				break
			# Notifying the user that the number they entered was negative
			elif number<0:
				print("Please enter positive numbers only. Please try again:")
				continue
			# Notifying the user that the number they entered exceeds the range
			elif number>255:
				print("Please enter numbers between 0 and 255 only. Please try again:")
				continue
		except:
			# Printing error message if exception occurs
			print("Please enter whole numbers only. Please try again:") 
	
