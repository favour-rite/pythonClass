
def future_investment (investment_amount,monthly_intrest,years):
	
	print (future_investment)
	return future_investment
print("Years\tFuture Value")
years = 1
investment = 0
monthly_interest_rate = 0
for count in range(1, years + 1):

      future_value = investment * ((1 + monthly_interest_rate) ** (12 * count))

      print(count, "\t\t", format(future_value, ".2f"))

investment = float(input("Enter the invesment amount: "))

interest = float(input("Enter the annual interest rate: "))

year = int(input("Enter the year: "))

future_investment(investment, interest/1200, year)

