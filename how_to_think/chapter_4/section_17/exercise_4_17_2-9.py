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


def day_add(start_day_name, delta):
    start_day_num = day_num(start_day_name)
    return day_name((start_day_num + delta) % len(week_days))


# tests
test_results = []

test_results.append(day_name(0) == "Sunday")
test_results.append(day_name(6) == "Saturday")

test_results.append(day_num("Sunday") == 0)
test_results.append(day_num("Saturday") == 6)

test_results.append(day_add("Monday", 4) ==  "Friday")
test_results.append(day_add("Tuesday", 0) == "Tuesday")
test_results.append(day_add("Tuesday", 14) == "Tuesday")
test_results.append(day_add("Sunday", 100) == "Tuesday")

for test, result in enumerate(test_results):
    print("Test", test, "was", result)
