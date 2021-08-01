def cutTheSticks(arr):
    print(len(arr))
    while len(arr) > 1:
        cutValue = min(arr)
        arr = list(map(lambda x: x - cutValue, arr))
        count = 0
        for item in arr:
            if item != 0:
                count += 1
        arr = list(filter(lambda x: x != 0, arr))
        if count != 0:
            print(count)


size = int(input())
array = [int(i) for i in input().split()]
cutTheSticks(array)
