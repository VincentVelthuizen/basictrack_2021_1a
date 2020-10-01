import turtle

screen = turtle.Screen()
poly = turtle.Turtle()

# Equilateral triangle
poly.color("red")
for _ in range(3):
    poly.forward(60)
    poly.left(120)

# Square
poly.color("orange")
for _ in range(4):
    poly.forward(90)
    poly.left(90)

# Hexagon
poly.color("green")
for _ in range(6):
    poly.forward(120)
    poly.left(60)

# Octagon
poly.color("blue")
for _ in range(8):
    poly.forward(150)
    poly.left(45)

screen.exitonclick()
