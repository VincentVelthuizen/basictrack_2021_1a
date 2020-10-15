import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

alex = tess
alex.color("hotpink")
tess.forward(1000)
alex.backward(1000)
# there will either be turtles, one moving forward and one moving back, or one first moving forward and then moving back

screen.exitonclick()
