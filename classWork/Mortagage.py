principal_amount = float (input ("Enter principal amount " ))
annual_intrest_rate = float (input("Enter annual intrest rate "))
duration = float (input ("Enter duration "))


monthly_rate = annual_intrest_rate / 100 / 12

number_of_months = duration * 12

numerator = monthly_rate * (1 + monthly_rate) ** number_of_months
denomerator = (1 + monthly_rate) ** number_of_months - 1 

monthly_payment = principal_amount * (numerator / denomerator ) 

print("Your monthly payment is $ " , monthly_payment )