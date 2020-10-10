def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return not is_even(number)


print(is_even(2))
print(is_even(3))
print(is_even(7))
print(is_even(8))

print(is_odd(2))
print(is_odd(3))
print(is_odd(7))
print(is_odd(8))
