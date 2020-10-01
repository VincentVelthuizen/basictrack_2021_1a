import turtle

side_length = 200
roof = (((side_length/2) ** 2) * 2) ** .5   # pythagoras

steps = [(90, side_length), (-90, side_length), (135, roof), (90, roof), (90, 2 * roof), (135, side_length),
         (135, 2 * roof), (135, side_length)]

screen = turtle.Screen()
pirate = turtle.Turtle()

for angle, distance in steps:
    pirate.left(angle)
    pirate.forward(distance)

screen.exitonclick()
