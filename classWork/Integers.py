number = int(input('enter five digit '))

number1 = number // 10000
number2 = number % 10000
number3= number2 // 1000
number4 = number2 %1000
number5 = number4 //100
number6 = number4 % 100
number7 = number6 // 10
number8= number6 %10
print(number1, number3, number5, number7, number8)