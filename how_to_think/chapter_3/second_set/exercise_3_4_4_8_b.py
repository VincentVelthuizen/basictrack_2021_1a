import turtle

screen = turtle.Screen()
poly = turtle.Turtle()

for _ in range(18):
    poly.forward(50)
    poly.left(360 / 18)

screen.exitonclick()
