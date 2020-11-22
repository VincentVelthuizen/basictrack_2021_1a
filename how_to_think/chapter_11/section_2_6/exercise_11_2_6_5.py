from how_to_think.chapter_11.section_1_12.Point import Point
from how_to_think.chapter_11.section_2_6.Rectangle import Rectangle

r = Rectangle(Point(), 10, 5)
r2 = Rectangle(Point(2, 2), 4, 4)

print(r.collides_with(r2))
print(r2.collides_with(r))

r2.corner = Point(.5, .5)
print(r.collides_with(r2))
print(r2.collides_with(r))

r2.corner = Point(-1, -1)
print(r.collides_with(r2))
print(r2.collides_with(r))

r2.corner = Point(9, -1)
print(r.collides_with(r2))
print(r2.collides_with(r))

r2.corner = Point(11, 0)
print(not r.collides_with(r2))
print(not r2.collides_with(r))

r2.corner = Point(0, -5)
print(not r.collides_with(r2))
print(not r2.collides_with(r))
