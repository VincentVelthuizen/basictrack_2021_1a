numbers = [1, 3, 4, 5]

sum_leading_odd_numbers = 0
for number in numbers:
    if number % 2 == 0:
        break
    sum_leading_odd_numbers += number

print(sum_leading_odd_numbers, "is the sum of the numbers up to but not including the first even number")
