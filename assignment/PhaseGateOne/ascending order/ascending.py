prompt user three times
compare each number to themselve 
print each accordingly
if fistnumber is less than second less than third
display result
then if firstnumber is less than thirdnumber less than second number
display result 
then if secondnumber is firstnumber less than thirdnumber
display result
then if secondnumber is less than thirdnumber less than firstnumber
then if thirdnumber is less than firstnumber less than second 
then third number is less than firtnumber less than second 

first_number = int (input("Enter first number: "))
second_number = int (input("Enter second number:"))
third_number = int (input("Enter third number: "))

if  first_number  < second_number < third_number :
	print("third_number ,second_number,first_number")

elif first_number <third_number < second_number:
	print(first_number,third_number,second_number)

elif second_number < first_number  < third_number:
	print(second_number ,first_number , third_number) 

elif second_number < third_number < first_number:
	print(second_number , third_number ,first_number) 

elif third_number  < first_number < second_number:  
	print(third_number,first_number , second_number) 
else:
	print(first_number, third_number ,second_number)
	
	

	print (" sorted order "  )