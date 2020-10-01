n = -24

count = 1
n = abs(n)  # get rid of a possible - sign
while n // 10 != 0:
    count += 1
    n = n // 10

print(n, "has", count, "digits")
