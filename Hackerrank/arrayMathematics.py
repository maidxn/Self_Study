import numpy as np


rows, columns = map(int, input().split())
array_A = np.array([input().split() for _ in range(rows)], int)
array_B = np.array([input().split() for _ in range(rows)], int)
print(np.add(array_A, array_B), np.subtract(array_A, array_B), np.multiply(array_A, array_B), sep='\n')
print(array_A // array_B, np.mod(array_A, array_B), np.power(array_A, array_B), sep='\n')
# In python 3, can use both buitl-in fuction or + - * /
