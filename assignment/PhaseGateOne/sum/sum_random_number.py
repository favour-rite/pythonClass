random numbers should be generated for users
for each number generated by random class should be sum up by the user
prompt user to enter addition od two number
if userinput is correct, then true
or it false


import random

add = 0
random_digit_one = random.randrange(1,60)
random_digit_two = random.randrange(0,100)
result = random_digit_one + random_digit_two 

print("sum the two numbers",random_digit_one, "and" ,random_digit_two )
user_Input = (input(" What is ur number "))


if user_Input == result:
	print("true")
else:
	print("false") 