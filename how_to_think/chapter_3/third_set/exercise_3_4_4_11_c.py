import turtle

side_length = 200
roof = (((side_length/2) ** 2) * 2) ** .5   # pythagoras

steps = [(90, side_length), (-90, side_length), (135, roof), (90, roof), (90, 2 * roof), (135, side_length),
         (135, 2 * roof), (135, side_length)]

screen = turtle.Screen()
bob = turtle.Turtle()   # the builder

for angle, distance in steps:
    bob.left(angle)
    bob.forward(distance)

screen.exitonclick()
