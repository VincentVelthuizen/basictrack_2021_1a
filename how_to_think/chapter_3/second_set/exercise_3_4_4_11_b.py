import turtle

screen = turtle.Screen()
cogsworth = turtle.Turtle()

screen.bgcolor("limegreen")

cogsworth.shape("turtle")
cogsworth.penup()
cogsworth.color("blue")
cogsworth.pensize(3)
cogsworth.left(90)

for _ in range(12):
    cogsworth.forward(150)
    cogsworth.pendown()
    cogsworth.forward(10)
    cogsworth.penup()
    cogsworth.forward(20)
    cogsworth.stamp()
    cogsworth.goto(0, 0)
    cogsworth.right(360 / 12)

screen.exitonclick()
