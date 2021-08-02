def ChocolateFeast(have, cost, wrapExchange):
    barEaten = have // cost
    wrap = barEaten
    while wrap >= wrapExchange:
        barEaten += wrap // wrapExchange
        wrap = wrap % wrapExchange + wrap // wrapExchange
    return barEaten


testCases = int(input())
for test in range(testCases):
    money, chocolateCost, wrappers = map(int, input().split())
    print(ChocolateFeast(money, chocolateCost, wrappers))



