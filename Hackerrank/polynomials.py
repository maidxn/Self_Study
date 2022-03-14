import numpy as np

poly = list(map(float, input().split()))
index = int(input())

# Or doesn't need variables
print(np.polyval(list(map(float, input().split())), int(input())))



