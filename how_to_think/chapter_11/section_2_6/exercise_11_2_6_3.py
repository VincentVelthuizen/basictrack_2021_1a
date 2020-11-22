from how_to_think.chapter_11.section_1_12.Point import Point
from how_to_think.chapter_11.section_2_6.Rectangle import Rectangle

r = Rectangle(Point(100, 50), 10, 5)
print(r.width == 10 and r.height == 5)
r.flip()
print(r.width == 5 and r.height == 10)
