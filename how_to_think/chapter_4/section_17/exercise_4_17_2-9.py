week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]


def day_name(day_number):
    if day_number < 0 or day_number > 6:
        return None
    else:
        return week_days[day_number]


def day_num(day_name):
    if day_name not in week_days:
        return None
    else:
        return week_days.index(day_name)


# tests
test_results = []

test_results.append(day_name(0) == "Sunday")
test_results.append(day_name(6) == "Saturday")

test_results.append(day_num("Sunday") == 0)
test_results.append(day_num("Saturday") == 6)

for test, result in enumerate(test_results):
    print("Test", test, "was", result)
