def countApplesAndOranges(s, t, a, b, apples, oranges):
    for index in range(len(apples)):
        apples[index] = apples[index] + a
    for index in range(len(oranges)):
        oranges[index] = oranges[index] + b
    count_a, count_o = 0, 0
    for apple in apples:
        if s <= apple <= t:
            count_a += 1
    print(count_a)
    for orange in oranges:
        if s <= orange <= t:
            count_o += 1
    print(count_o)


s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apples = [int(i) for i in input().split()]
oranges = [int(i) for i in input().split()]
countApplesAndOranges(s, t, a, b, apples, oranges)

