import turtle


def draw_poly(animal, sides, size):
    for _ in range(sides):
        animal.forward(size)
        animal.left(360 / sides)


screen = turtle.Screen()
poly = turtle.Turtle()

draw_poly(poly, 8, 50)

screen.exitonclick()
