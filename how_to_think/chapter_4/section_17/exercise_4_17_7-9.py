def to_secs(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


# tests
test_results = []

test_results.append(to_secs(2, 30, 10) == 9010)
test_results.append(to_secs(2, 0, 0) == 7200)
test_results.append(to_secs(0, 2, 0) == 120)
test_results.append(to_secs(0, 0, 42) == 42)
test_results.append(to_secs(0, -10, 10) == -590)

for test, result in enumerate(test_results):
    print("Test", test, "was", result)
