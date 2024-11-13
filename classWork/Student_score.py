number_of_pass = 0
number_of_fail = 0
for Student_input in range(1,15):

 Student_input= int(input("Enter Score"))

 if Student_input >= 45:
  print("pass")

 elif Student_input < 45:
  print ("fail")
print(f'number of student fail and number of student pass' )