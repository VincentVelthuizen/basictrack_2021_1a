numbers = [1, 2, 3, 4, 5, 6]

no_odd_numbers = 0  # no is short for "number of"
for number in numbers:
    if number % 2 != 0:
        no_odd_numbers += 1

print("There are", no_odd_numbers, "odd numbers in the list")
