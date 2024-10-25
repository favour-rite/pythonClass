User_input = int(input("Enter three numbers "))

number = User_input 
num = number % 10
second_number = number // 10
remainder = second_number % 10
last_number = second_number // 10

if  last_number == num :
	print(" is a parlindrome " )
	
else:
	print("is not a parlindrome " )
