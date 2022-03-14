import numpy as np
np.set_printoptions(legacy='1.13')

size = int(input())
arr = np.array([input().split() for _ in range(size)], float)
print(np.linalg.det(arr))
