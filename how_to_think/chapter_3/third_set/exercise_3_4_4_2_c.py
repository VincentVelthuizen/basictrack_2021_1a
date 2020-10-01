numbers = [1, 2, 3, 4, 5, 6]

sum_even_numbers = 0
for number in numbers:
    if number % 2 == 0:
        sum_even_numbers += number

print(sum_even_numbers, "is the sum of the even numbers in the list")
