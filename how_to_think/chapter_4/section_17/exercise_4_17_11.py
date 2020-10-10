def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


print(compare(5, 4))
print(compare(7, 7))
print(compare(2, 3))
print(compare(42, 1))
