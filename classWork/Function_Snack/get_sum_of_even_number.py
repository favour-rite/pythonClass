def sum_of_even(numbers):

	sum = 0
	number = {1,2,3,4,5}

	for number in number:
		if number % 2 == 0:
			sum+=number
			return sum