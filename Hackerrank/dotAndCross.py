import numpy as np

size = int(input())
arr_A = np.array([input().split() for _ in range(size)], int)
arr_B = np.array([input().split() for _ in range(size)], int)

print(np.dot(arr_A, arr_B))
