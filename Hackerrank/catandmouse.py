def catAndMouse(a, b, c):
    difAC = abs(a - c)
    difBC = abs(b - c)
    if difAC == difBC:
        print("Mouse C")
    elif difAC < difBC:
        print("Cat A")
    else:
        print("Cat B")


queries = int(input())
count = 0
while count < queries:
    catA, catB, mouseC = map(int, input().split())
    count += 1
    catAndMouse(catA, catB, mouseC)
