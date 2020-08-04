# Function reverses the list
def reverse_list(original_list) :
	reversedList=[]
	# Reversing the binaryList
	for i in range((len(original_list)-1),-1,-1):
		reversedList.append(original_list[i])
		
	#Returning the binaryList when the function is called
	return reversedList


