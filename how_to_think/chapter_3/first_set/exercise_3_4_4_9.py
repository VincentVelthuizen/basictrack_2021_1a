a = 5
b = 3
c = 4

if a > c:
    a, c = c, a     # swap values of a and c so a is smaller than c

if b > c:
    b, c = c, b     # swap values of b and c so b is smaller than c

# c must now be the largest value of the set

hypotenuse = (a * a + b * b) ** .5

# The exercise asks for a function but we will not talk about functions until next week
# This solution therefor is not exactly what the exercise asked for but it is in the same spirit
if abs(c - hypotenuse) < 1e-7:
    print("The triangle is right-angled")
else:
    print("This is not a right-angled triangle")
