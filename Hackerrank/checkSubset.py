def CheckSubset(arr_1, arr_2):
    return True if arr_1.issubset(arr_2) else False


testCases = int(input())
for testCase in range(testCases):
    sizeA = int(input())
    arrayA = set(map(int, input().split()))
    sizeB = int(input())
    arrayB = set(map(int, input().split()))
    print(CheckSubset(arrayA, arrayB))
