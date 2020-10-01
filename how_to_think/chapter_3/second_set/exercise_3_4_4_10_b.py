import turtle

screen = turtle.Screen()
don = turtle.Turtle()   # Starry, starry night

don.left(36)
for _ in range(5):
    don.forward(100)
    don.left(180 - 36)

don.hideturtle()

screen.exitonclick()
