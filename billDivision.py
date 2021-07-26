def bonAppetit(arr, index, portion):
    pos = 0
    total = 0
    for item in arr:
        if pos == index:
            pos += 1
            continue
        pos += 1
        total += item
    if portion == (total / 2):
        print("Bon Appetit")
    else:
        print(portion - total // 2)


numberOfItems, declineItem = map(int, input().split())
items = [int(i) for i in input().split()]
cost = int(input())
bonAppetit(items, declineItem, cost)
