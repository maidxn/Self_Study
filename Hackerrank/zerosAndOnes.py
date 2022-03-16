import numpy as np


dimensions = tuple(map(int, input().split()))
print(np.zeros(dimensions, int))
print(np.ones(dimensions, int))