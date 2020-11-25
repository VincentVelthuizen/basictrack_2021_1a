from how_to_think.chapter_11.section_3_11.MyTime import MyTime

time1 = MyTime(1, 30, 0)
time2 = MyTime(2, 0, 0)
time3 = MyTime(2, 30, 0)

print(time2.between(time1, time3))  # should be True
print(time1.between(time2, time3))  # should be False
