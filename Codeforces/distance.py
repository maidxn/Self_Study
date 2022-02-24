def FindBisectingPoint(x, y):
    distance = (x + y) // 2
    for value in range(0, distance + 1):
        if abs(x - value) + abs(y - (distance - value)) == distance:
            return value, distance - value
    return -1, -1


testCase = int(input())
for each in range(testCase):
    x_value, y_value = map(int, input().split())
    print(*FindBisectingPoint(x_value, y_value))

