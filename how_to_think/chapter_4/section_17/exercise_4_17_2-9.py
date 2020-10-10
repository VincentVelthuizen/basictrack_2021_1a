week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


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


def days_in_month(month_name):
    if month_name not in month_names:
        return None
    else:
        return month_length[month_names.index(month_name)]


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

test_results.append(day_add("Sunday", -1) == "Saturday")
test_results.append(day_add("Sunday", -7) == "Sunday")
test_results.append(day_add("Tuesday", -100) == "Sunday")

test_results.append(days_in_month("February") == 28)
test_results.append(days_in_month("December") == 31)

for test, result in enumerate(test_results):
    print("Test", test, "was", result)
