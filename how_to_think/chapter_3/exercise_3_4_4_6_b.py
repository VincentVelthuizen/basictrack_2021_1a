import turtle

screen = turtle.Screen()
pirate = turtle.Turtle()

steps = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for step in steps:
    pirate.left(step)
    pirate.forward(100)

screen.exitonclick()
