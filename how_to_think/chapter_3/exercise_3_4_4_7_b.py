import turtle

screen = turtle.Screen()
pirate = turtle.Turtle()

steps = [160, -43, 270, -97, -43, 200, -940, 17, -86]

heading = 0
for step in steps:
    pirate.left(step)
    pirate.forward(100)
    heading += step

print("The final heading is", heading % 360)

screen.exitonclick()
