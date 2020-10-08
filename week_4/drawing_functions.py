import turtle


# non-fruitful function
def draw_square(animal, size):
    """
    Draw a square
    """
    for _ in range(4):
        animal.forward(size)
        animal.left(90)


# fruitful
def calculate_surface_of_square(side_length):
    surface = side_length ** 2
    print("17", surface)
    return surface


screen = turtle.Screen()
nick = turtle.Turtle()

for step in range(6):  # range(6) -> [0, 1, 2, 3, 4, 5]
    draw_square(nick, step * 5)
    nick.left(6)

    result = calculate_surface_of_square(step * 5)
    print("29", result)

screen.exitonclick()
