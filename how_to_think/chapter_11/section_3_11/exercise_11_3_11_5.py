from how_to_think.chapter_11.section_3_11.MyTime import MyTime

time1 = MyTime()

print(time1)    # Should be 00:00:00
time1.increment(7328)   # add two hours, 2 minutes and 8 seconds
print(time1)    # Should be 02:02:08
time1.increment(-6)
print(time1)    # Should be 02:02:02
time1.increment(-58)
print(time1)    # Should be 02:01:04
