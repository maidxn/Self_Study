def getMoneySpent(arr1, arr2, total):
    res = []
    for item in arr1:
        for second_item in arr2:
            sum_two_things = item + second_item
            if sum_two_things <= total:
                res.append(sum_two_things)
    if not res:
        return -1
    ans = res[0]
    for price in res:
        if price > ans:
            ans = price
    return ans


budget, nKeyBoard, nUsb = map(int, input().split())
keyBoards = [int(i) for i in input().split()]
usbs = [int(i) for i in input().split()]
print(getMoneySpent(keyBoards, usbs, budget))
