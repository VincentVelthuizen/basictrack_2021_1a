from how_to_think.chapter_11.section_1_12.Point import Point


def distance(point_a, point_b):
    delta_x = point_a.x - point_b.x
    delta_y = point_a.y - point_b.y
    return (delta_x ** 2 + delta_y ** 2) ** .5


if __name__ == "__main__":
    point_1 = Point(1, 4)
    point_2 = Point(4, 8)
    print(distance(point_1, point_2))
