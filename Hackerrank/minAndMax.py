import numpy as np


rows, columns = map(int, input().split())
arr = []
for row in range(rows):
    arr.append(list(map(int, input().split())))

# Or
numpy_arr = np.array([input().split() for _ in range(rows)], int)
print(np.max(np.min(np.array(numpy_arr), axis=1)))
