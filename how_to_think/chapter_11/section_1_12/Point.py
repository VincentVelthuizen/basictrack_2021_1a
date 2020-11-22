class Point:
    """ Point class represents and manipulates x, y coordinates. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def distance_from_origin(self):
        return (self.x * self.x + self.y * self.y) ** .5

    def reflect_x(self):
        return Point(self.x, -1 * self.y)

    def slope_from_origin(self):
        # this will fail if x == 0
        return self.y / self.x

    def get_line_to(self, other_point):
        delta_x = other_point.x - self.x
        delta_y = other_point.y - self.y

        # this will fail if delta_x == 0
        b = delta_y / delta_x
        c = self.y - (b * self.x)

        return b, c

    def midpoint(self, other_point):
        x = (self.x + other_point.x) / 2
        y = (self.y + other_point.y) / 2
        return Point(x, y)

    def get_perpendicular_bisector(self, other_point):
        gradient, _ = self.get_line_to(other_point)
        midpoint = self.midpoint(other_point)
        bisector_gradient = gradient / -1
        c = midpoint.y - (bisector_gradient * midpoint.x)
        return bisector_gradient, c
