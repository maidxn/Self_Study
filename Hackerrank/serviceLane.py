def ServiceLane(s, e, arr):
    return min(arr[s:e+1])


numberOfWWidths, numberOfCases = map(int, input().split())
widthArray = [int(i) for i in input().split()]

for i in range(numberOfCases):
    start, end = map(int, input().split())
    print(ServiceLane(start, end, widthArray))
