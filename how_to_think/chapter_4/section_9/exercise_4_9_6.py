import turtle


def draw_poly(animal, sides, size):
    for _ in range(sides):
        animal.forward(size)
        animal.left(360 / sides)


def draw_equitriangle(animal, size):
    draw_poly(animal, 3, size)


screen = turtle.Screen()
poly = turtle.Turtle()

draw_equitriangle(poly, 150)

screen.exitonclick()
