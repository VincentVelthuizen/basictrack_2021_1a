numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,49.9, 45, 44.9, 40, 39.9, 2, 0]

for mark in numbers:
    if mark >= 75:
        grade = "First"
    elif mark >= 70:
        grade = "Upper Second"
    elif mark >= 60:
        grade = "Second"
    elif mark >= 50:
        grade = "Third"
    elif mark >= 45:
        grade = "F1 Supp"
    elif mark >= 40:
        grade = "F2"
    else:
        grade = "F3"
    print(mark, grade)
