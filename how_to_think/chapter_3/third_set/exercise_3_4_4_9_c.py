candidate = 37

for divisor in range(2, candidate // 2):
    if candidate % divisor == 0:
        print(divisor, "is a divisor of", candidate, "therefor it is not prime")
        print(False)
        break
else:   # Note the else is at the "for-level" not at the "if-level"!
    print("No divisor found for", candidate, "therefor it is prime")
    print(True)
