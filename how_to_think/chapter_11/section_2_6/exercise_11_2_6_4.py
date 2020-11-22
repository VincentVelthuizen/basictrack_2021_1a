from how_to_think.chapter_11.section_1_12.Point import Point
from how_to_think.chapter_11.section_2_6.Rectangle import Rectangle


def test(test_result):
    print("Test has {}".format("succeeded" if test_result else "failed"))


r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))
