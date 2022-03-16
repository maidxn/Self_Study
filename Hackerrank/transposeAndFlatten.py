import numpy as np


rows, columns = map(int, input().split())
arr = np.array([input().split() for _ in range(rows)], int)
print(np.transpose(arr), arr.flatten(), sep='\n')
