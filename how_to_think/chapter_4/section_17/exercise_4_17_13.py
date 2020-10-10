def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def intercept(x1, y1, x2, y2):
    # ax + b
    a = slope(x1, y1, x2, y2)
    b = y1 - (x1 * a)
    return b


print(slope(5, 3, 4, 2))
print(slope(1, 2, 3, 2))
print(slope(1, 2, 3, 3))
print(slope(2, 4, 1, 2))

print()

print(intercept(1, 6, 3, 12))
print(intercept(6, 1, 1, 6))
print(intercept(4, 6, 12, 8))
