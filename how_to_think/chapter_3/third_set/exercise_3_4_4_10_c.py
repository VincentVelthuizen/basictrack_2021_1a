import turtle

steps = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

screen = turtle.Screen()
pirate = turtle.Turtle()

for angle, distance in steps:
    pirate.left(angle)
    pirate.forward(distance)

screen.exitonclick()
