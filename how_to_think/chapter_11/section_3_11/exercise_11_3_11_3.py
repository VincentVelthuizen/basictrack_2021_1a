from how_to_think.chapter_11.section_3_11.MyTime import MyTime

time1 = MyTime(1, 30, 0)
time2 = MyTime(2, 0, 0)

print(time1 > time2)    # should be False
print(time2 > time1)    # should be True
