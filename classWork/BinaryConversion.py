integer = (input("Enter number: "))

binary_conversion = ""

while integer > 0:
	remaining = integer % 2
	binary_conversion = str(remaining ) + binary_conversion
	integer = integer // 2

print(binary_conversion)