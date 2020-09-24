principal_amount = float(input("What is the principal amount?"))
frequency = int(input("How many times per year is the interest compounded?"))
interest_rate = float(input("What is the interest rate (per year, as a decimal)"))
duration = int(input("For what number of years would you like to calculate the compound interest?"))

final_amount = principal_amount * (1 + (interest_rate/frequency)) ** (frequency * duration)

print("The final amount is:", final_amount)
