from itertools import product


firstArray = list(map(int, input().split()))
secondArray = list(map(int, input().split()))
print(*product(firstArray, secondArray))
