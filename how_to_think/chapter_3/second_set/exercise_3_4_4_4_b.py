numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for number in numbers:
    print(number)

for number in numbers:
    print(number, number ** 2)

total = 0
for number in numbers:
    total += number
print(total)

product = 1
for number in numbers:
    product *= number
print(product)
