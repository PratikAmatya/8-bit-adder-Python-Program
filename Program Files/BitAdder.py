# Bit adder

#Importing ReverseList module as reverse
import ReverseList as reverse

# bit_add module that returns the sum of two binary numbers 
def bit_add(list1,list2):
	carry_in=0
	total_sum=0
	binarysum_list=[]
	carry_out=0
	
	# For loop
	for i in range(7,-1,-1):
		a=list1[i]
		b=list2[i]
		if i==7:
			# Using Half Adder for the last digits of the two binary numbers to find the total_sum and the carry_out
			total_sum=a^b
			carry_out=a&b
		else:
			# Using Full Adder to find the total_sum and the carry_out
			total_sum=a^(b^carry_in)
			carry_out=(carry_in&(a^b))|(a&b)
		carry_in=carry_out
		# Adding total_sum to the binarysum_list
		binarysum_list.append(total_sum)
		# Adding the carry_out at the end as well
		if i == 0:
			binarysum_list.append(carry_out)
	# To reverse the list		
	binarysum_list=reverse.reverse_list(binarysum_list)	
	
	binary_sum=""
	
	# For loop
	for binaryDigit in binarysum_list:
		binary_letter=str(binaryDigit)
		binary_sum=binary_sum+binary_letter
	
	# String to Int Conversion
	binary_sum=int(binary_sum)
		
	#Returning binary_sum when the function is called
	return binary_sum
