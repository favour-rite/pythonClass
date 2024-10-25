User_weight = int (input("weight in pounds "))

User_inches = int (input ("height in inches "))
 
killogram = int(input("weight in kilogram ")) 
meters = int(input("height in meters "))

bmi =( User_weight * 703 / User_inches * User_inches )
bmi2 = killogram / meters * meters

print(bmi)
print (bmi2) 