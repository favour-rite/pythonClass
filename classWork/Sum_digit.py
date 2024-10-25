number = int(input("Enter an integer between 0 and 1000: "))
if (number < 1000 and number > 0):
	first_number = number // 100
	second_number = (number // 10)%10
	
	third_number = number % 10
	sum = first_number + second_number + third_number
	print(sum)
else:
	print ("Number entered is not valid")