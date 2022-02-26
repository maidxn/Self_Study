def FindChocolatesCanBuy(arr, low, high, budget):
    arr = sorted(arr)
    if arr[0] > high:
        return 0
    count = 0
    spend = 0
    for each in arr:
        if low <= each <= high and spend + each <= budget:
            count += 1
            spend += each
    return count


testCases = int(input())
for testCase in range(testCases):
    size, cheap, expensive, money = map(int, input().split())
    chocolates = list(map(int, input().split()))
    print(FindChocolatesCanBuy(chocolates, cheap, expensive, money))
