def TaumBday(b, w, bc, wc, z):
    changeB, changeW = -1, -1
    if bc + z < wc:
        changeW = bc + z
    if wc + z < bc:
        changeB = wc + z
    total = 0
    if changeB != -1:
        total += b * changeB
    else:
        total += b * bc
    if changeW != -1:
        total += w * changeW
    else:
        total += w * wc
    return total


testCases = int(input())
for test in range(testCases):
    numberBlack, numberWhite = map(int, input().split())
    blackCost, whiteCost, exchange = map(int, input().split())
    print(TaumBday(numberBlack, numberWhite, blackCost, whiteCost, exchange))


