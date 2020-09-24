principal_amount = 10000
frequency = 1
interest_rate = .01
duration = 10

final_amount = principal_amount * (1 + (interest_rate/frequency)) ** (frequency * duration)

print("The final amount is:", final_amount)