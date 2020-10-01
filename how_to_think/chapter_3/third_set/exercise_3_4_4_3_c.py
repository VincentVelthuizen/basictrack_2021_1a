numbers = [1, -2, -3, 4, 5, -6]

sum_negative_numbers = 0  # no is short for "number of"
for number in numbers:
    if number < 0:
        sum_negative_numbers += number

print(sum_negative_numbers, "is the sum of all negative numbers in the list")
