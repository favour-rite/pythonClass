
number = int(input(" enter number "))
digit1 = number % 10
digit2 = number // 10
digit3 = digit2 % 10
digit4 = digit2 // 10
if digit1 == digit4:
	print("is palindrome")
else:
	print("is not palindrome")