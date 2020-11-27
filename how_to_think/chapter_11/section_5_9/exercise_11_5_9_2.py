import turtle

from how_to_think.chapter_11.section_5_9.TurtleGTX import TurtleGTX

ninja = TurtleGTX()
screen = turtle.Screen()

for i in range(50):
    try:
        ninja.forward(i * 2)
        ninja.left(90)
    except AssertionError:
        print("Changed the tyre at", ninja.odo_meter)
        ninja.change_tyre()

screen.exitonclick()
