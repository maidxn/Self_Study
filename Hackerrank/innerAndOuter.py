import numpy as np

array_A = np.array([input().split()], int)
array_B = np.array([input().split()], int)

print(np.inner(array_A, array_B)[0][0], np.outer(array_A, array_B), sep='\n')
