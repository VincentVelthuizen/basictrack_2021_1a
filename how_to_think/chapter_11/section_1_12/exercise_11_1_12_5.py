import math
from random import random

from how_to_think.chapter_11.section_1_12.Point import Point


def intersect(line_1, line_2):
    b_1, c_1 = line_1
    b_2, c_2 = line_2

    x = (c_2 - c_1) / (b_1 - b_2)
    y = b_1 * x + c_1

    return Point(x, y)


def random_point_on_circle(circle_center=Point()):
    angle = random() * math.tau
    return Point(math.cos(angle) + circle_center.x, math.sin(angle) + circle_center.y)


center = Point(2, 4)
point_a = Point(1 + center.x, 0 + center.y)
point_b = Point(0 + center.x, -1 + center.y)
point_c = Point(1 + center.x, 0 + center.y)
point_d = Point(0 + center.x, 1 + center.y)

# This code does not appear to work with the random points on a circle
# at this point it is not clear to me if the random points or the algorithm
# for finding the center is at fault.
# I'll have to come back to it later.
# point_a = random_point_on_circle(center)
# point_b = random_point_on_circle(center)
# point_c = random_point_on_circle(center)
# point_d = random_point_on_circle(center)

line_a = point_a.get_perpendicular_bisector(point_b)
line_c = point_c.get_perpendicular_bisector(point_d)

print(intersect(line_a, line_c))
