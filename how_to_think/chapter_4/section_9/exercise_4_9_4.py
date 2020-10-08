import turtle


def draw_poly(animal, sides, size):
    for _ in range(sides):
        animal.forward(size)
        animal.left(360 / sides)


screen = turtle.Screen()
poly = turtle.Turtle()

number_of_squares = 20
for _ in range(number_of_squares):
    draw_poly(poly, 4, 50)
    poly.left(360 / number_of_squares)

screen.exitonclick()
