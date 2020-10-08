import turtle


def draw_square(animal):
    for _ in range(4):
        animal.forward(20)
        animal.left(90)


screen = turtle.Screen()
poly = turtle.Turtle()

for _ in range(5):
    draw_square(poly)
    poly.penup()
    poly.forward(40)
    poly.pendown()

screen.exitonclick()
