def HowManyGames(baseCost, discountCost, minimunCost, budget):
    games = 0
    currMoney = budget
    cost = baseCost
    while currMoney >= cost:
        #print("Current cos is", cost)
        #print("Current money is", currMoney)
        games += 1
        currMoney -= cost
        if cost - discountCost > minimunCost:
            cost -= discountCost
        else:
            cost = minimunCost
    return games


firstCost, discount, minCost, startBudget = map(int, input().split())
print(HowManyGames(firstCost, discount, minCost, startBudget))
