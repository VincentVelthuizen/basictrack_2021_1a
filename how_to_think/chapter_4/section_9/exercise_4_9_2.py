import turtle


def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)


def move_turtle(animal, left, down):
    animal.penup()
    animal.right(90)
    animal.forward(down)
    animal.left(90)
    animal.backward(left)
    animal.pendown()


screen = turtle.Screen()
poly = turtle.Turtle()

for i in range(5):
    draw_square(poly, (i + 1) * 20)
    move_turtle(poly, 10, 10)

screen.exitonclick()
