from collections import deque

array = deque()
numberOfOperations = int(input())

for operation in range(numberOfOperations):
    method = input()
    if method == "pop":
        array.pop()
    elif method == "popleft":
        array.popleft()
    else:
        method, number = method.split()
        if method == "append":
            array.append(int(number))
        else:
            array.appendleft(int(number))
print(*array, sep=" ")
