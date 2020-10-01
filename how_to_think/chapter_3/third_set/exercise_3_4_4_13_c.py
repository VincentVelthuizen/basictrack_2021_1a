n = -24567876
original_n = n

count = 1
n = abs(n)  # get rid of a possible - sign
while n // 10 != 0:
    if (n % 10) % 2 == 0:
        count += 1
    n = n // 10

print(original_n, "has", count, "even digits")
