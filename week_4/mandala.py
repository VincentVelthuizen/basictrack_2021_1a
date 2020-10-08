import turtle, math, random


# https://stackoverflow.com/questions/7198144/how-to-draw-a-n-sided-regular-polygon-in-cartesian-coordinates#7198179
def polygon(michelangelo, number_of_sides, radius, center_x=0, center_y=0):

    for n in range(number_of_sides + 1):
        x_coordinate = radius * math.cos(2 * math.pi * n/number_of_sides)
        y_coordinate = radius * math.sin(2 * math.pi * n/number_of_sides)
        michelangelo.setposition(x_coordinate + center_x, y_coordinate + center_y)
        michelangelo.pendown()

    michelangelo.penup()


mandala = turtle.Screen()
mandala.bgcolor('cyan')

monk = turtle.Turtle()

monk.penup()

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

for x in reversed(range(3, 14)):
    monk.fillcolor(colors[x % len(colors)])
    monk.begin_fill()
    polygon(monk, x, 4 * (1.44 ** x))
    monk.end_fill()

monk.hideturtle()
mandala.exitonclick()
