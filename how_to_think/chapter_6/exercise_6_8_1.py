import numpy as np

a = np.array(list(range(32)), dtype='uint8')
string_format = "{:>4}" * 32

for _ in range(9):
    print(string_format.format(*a))
    a += 32
