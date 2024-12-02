def get_sum_and_remove(number):
	add = 0 
	v = 0
	for count in number:
		add += sum(number) - number[v]
		v+=1
	return add