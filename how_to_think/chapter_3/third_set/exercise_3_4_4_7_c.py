n = 25
threshold = 1e-7
approximation = n / 25

while True:
    better = (approximation + (n / approximation)) / 2
    print("approximation:", better)
    if abs(approximation - better) < threshold:
        print("Best:", better)
        break
    approximation = better
