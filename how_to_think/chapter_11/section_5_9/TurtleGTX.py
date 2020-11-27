import random
from turtle import Turtle


class TurtleGTX(Turtle):

    def __init__(self):
        super().__init__()
        self.odo_meter = 0
        self.broken_down = False

    def jump(self, distance) -> None:
        pen = self.isdown()
        self.penup()
        self.forward(distance)
        if pen:
            self.pendown()

    def forward(self, distance: float) -> None:
        if self.broken_down:
            raise AssertionError("This turtle has broken down, please change the tyre.")
        self.odo_meter += abs(distance)
        super().forward(distance)
        if random.random() * 1000 < self.odo_meter:
            print("Breaking down")
            self.broken_down = True

    def change_tyre(self):
        self.broken_down = False
        self.odo_meter = 0
