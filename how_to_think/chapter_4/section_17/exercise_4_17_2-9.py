week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]


def day_name(day_number):
    if day_number < 0 or day_number > 6:
        return None
    else:
        return week_days[day_number]


# tests
test_results = []

test_results.append(day_name(0) == "Sunday")
test_results.append(day_name(6) == "Saturday")

for test, result in enumerate(test_results):
    print("Test", test, "was", result)
