




for count in range(0,7):
	for number in range(0, 7-count):
		print(' ', end = "")
	for nums in range(0,count):
		print(1,end='')
	for nums in range(0,count):
		print(1,end='')
	for number in range(0, 7-count):
		print(' ', end = "")
	print()

for count in range(0,7):
	for number in range(0, count):
		print(' ', end = "")
	for nums in range(0,7-count):
		print(1,end='')
	for nums in range(0, 7-count):
		print(1,end='')
	for number in range(0,count):
		print(' ', end = "")
