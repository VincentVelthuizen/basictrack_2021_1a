def to_secs(hours, minutes, seconds):
    return int(hours * 3600 + minutes * 60 + seconds)


def hours_in(seconds):
    return seconds // 3600


def minutes_in(seconds):
    return (seconds % 3600) // 60  # first get rid of the whole hours, then check how many minutes are left


def seconds_in(seconds):
    return seconds % 60

# tests
test_results = []

test_results.append(to_secs(2, 30, 10) == 9010)
test_results.append(to_secs(2, 0, 0) == 7200)
test_results.append(to_secs(0, 2, 0) == 120)
test_results.append(to_secs(0, 0, 42) == 42)
test_results.append(to_secs(0, -10, 10) == -590)

test_results.append(to_secs(2.5, 0, 10.71) == 9010)
test_results.append(to_secs(2.433,0,0) == 8758)

test_results.append(hours_in(9010) == 2)
test_results.append(minutes_in(9010) == 30)
test_results.append(seconds_in(9010) == 10)

for test, result in enumerate(test_results):
    print("Test", test, "was", result)
