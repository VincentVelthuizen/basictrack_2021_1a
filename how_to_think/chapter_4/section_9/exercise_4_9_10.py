import turtle


def draw_star(animal, size):
    for _ in range(5):
        animal.forward(size)
        animal.left(144)


screen = turtle.Screen()
poly = turtle.Turtle()

poly.left(36)

for _ in range(5):
    draw_star(poly, 100)

    poly.penup()
    poly.forward(350)
    poly.left(144)
    poly.pendown()

screen.exitonclick()
