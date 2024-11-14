
import random

def math_quiz():
	right_answer = []
	sign = ["+","+","+","+","+","*","*","*","-","-"]
	count = 0
	passed = 0
	failed = 0

	while counter < 10:
		rand1 = random.randrange(1,1000)
		rand2 = random.randrange(1,1000)
		
		response = int(input(f"Calculate {rand1} {sign[count]} {rand2}: "))
		if count < 5:
			answer = rand1 + rand2
		elif count >= 5 and count <= 7:
			answer = rand1 * rand2
		elif count >=8 :
			answer = rand1 - rand2
		
		if answer == response:
			passed += 1

		else: 
			failed += 1
			right_answer.append(f"You missed question {count 
+1}, The correct answer for {rand1} {sign[count]} {rand2} is {answer}")

		count +=1
			
	for result in right_answer:
		print(result)

	return (f"Your score is {passed} / {failed}")

print(math_quiz())