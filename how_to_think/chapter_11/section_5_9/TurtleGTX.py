from turtle import Turtle


class TurtleGTX(Turtle):

    def __init__(self):
        super().__init__()
        self.odo_meter = 0

    def jump(self, distance):
        pen = self.isdown()
        self.penup()
        self.forward(distance)
        if pen:
            self.pendown()

    def forward(self, distance: float) -> None:
        self.odo_meter += abs(distance)
        super().forward(distance)
