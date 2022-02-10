toys, budget = map(int, input().split())
toyArr = list(map(int, input().split()))
if sum(toyArr) <= budget:
    print(len(toyArr))
else:
    toyArr = sorted(toyArr)
    if toyArr[0] > budget:
        print(0)
    else:
        count = 0
        money = 0
        for toy in toyArr:
            if money + toy < budget:
                money += toy
                count += 1
        print(count)

