a = 3
b = 4
c = 6

hypotenuse = (a * a + b * b) ** .5

# The exercise asks for a function but we will not talk about functions until next week
# This solution therefor is not exactly what the exercise asked for but it is in the same spirit
if abs(c - hypotenuse) < 1e-7:
    print("The triangle is right-angled")
else:
    print("This is not a right-angled triangle")
