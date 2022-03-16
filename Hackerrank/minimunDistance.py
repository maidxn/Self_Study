def MinimumDistances(arr):
    stored = {}
    for index in range(len(arr)):
        if arr[index] not in stored.keys():
            stored[arr[index]] = [index]
        else:
            stored[arr[index]].append(index)
    index_compare = []
    for index_list in stored.values():
        if len(index_list) == 2:
            index_compare.append(index_list)
    if not index_compare:
        return -1
    else:
        distance = list(map(lambda x: abs(x[0] - x[1]), index_compare))
        return min(distance)


size = int(input())
array = [int(i) for i in input().split()]
print(MinimumDistances(array))
