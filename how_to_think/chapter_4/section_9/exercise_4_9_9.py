import turtle


def draw_star(animal, size):
    for _ in range(5):
        animal.forward(size)
        animal.left(144)


screen = turtle.Screen()
poly = turtle.Turtle()

poly.left(36)
draw_star(poly, 100)

screen.exitonclick()
