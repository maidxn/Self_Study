import numpy as np


row, column = map(int, input().split())
array = np.array([input().split() for _ in range(row)], int)
print(np.mean(array, axis=1), np.var(array, axis=0), sep='\n')
# I don't know why this problem doesn't work well with no.set_printoption()
# I just came up with round :)
print(round(np.std(array), 11))
