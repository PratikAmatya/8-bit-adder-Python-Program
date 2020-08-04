# Importing the required module
import ReverseList as reverse

#Decimal to binary conversion function
def decimal_to_binary(firstNumVariable):	
	binaryList=[]
	# While Loop
	while firstNumVariable>0:
		# Adding 0 to the binaryList if the remainder when divided by 2 is 0
		if firstNumVariable%2==0:
			binaryList.append(0)
		# Adding 1 to the binaryList if the remainder when divided by 2 is not 0
		else:
			binaryList.append(1)
		firstNumVariable=firstNumVariable//2
	
	# Making the binaryList containing 8 items if it is not
	if len(binaryList)!=8:
		loopNumber=8-len(binaryList)
		for i in range(loopNumber):
			binaryList.append(0)
	# To reverse the list	
	binaryList=reverse.reverse_list(binaryList)
	#Returning the lists
	return binaryList



	
