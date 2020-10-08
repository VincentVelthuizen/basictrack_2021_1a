import time
import turtle


screen = turtle.Screen()
poly = turtle.Turtle()

number_of_revolutions = 20
for i in range(number_of_revolutions * 4):
    poly.forward(i * 3)
    poly.right(90)

# wait for 2 seconds
time.sleep(2)
poly.setposition(0, 0)
screen.clear()

for i in range(number_of_revolutions * 4):
    poly.forward(i * 3)
    poly.right(89)

screen.exitonclick()
