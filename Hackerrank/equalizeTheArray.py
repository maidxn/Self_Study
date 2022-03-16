def EqualizeTheArray(arr):
    record = {}
    for item in arr:
        if item not in record.keys():
            record[item] = 1
        else:
            record[item] += 1
    return len(arr) - max(record.values())


size = int(input())
array = [int(i) for i in input().split()]
print(EqualizeTheArray(array))
