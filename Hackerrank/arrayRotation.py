def CircularArrayRotation(arr, n, pos):
    n = n % len(arr)
    for time in range(n):
        arr.insert(0, arr[-1])
        arr.pop(-1)
    for index in pos:
        print(arr[index])


numberOfElements, rotationTimes, numberOfQueries = map(int, input().split())
array = [int(i) for i in input().split()]
queries = []

for item in range(numberOfQueries):
    queries.append(int(input()))

CircularArrayRotation(array, rotationTimes, queries)

