prompt user to enter number between 0 and 1000
if number less than 1000 and numbe greater than 0
number divide 100
number divide 100 then you divide by 10 using mod
thr remainder mod 10
add all the number extracted
else if input is is above invalid 





number = int(input("Enter an integer between 0 and 1000: "))
if (number < 1000 and number > 0):
	first_number = number // 100
	second_number = (number // 10) % 10
	
	third_number = number % 10
	sum = first_number + second_number + third_number
	print(sum)

else:
	print ("Number entered is not valid")