import numpy as np

a = np.array([230, 10, 284, 39, 76, 60])

while min(a) < 100:
    a[a < 100] *= 2
    print(a)

print(a[(a > 150) & (a < 200)])
