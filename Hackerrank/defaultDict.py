from collections import defaultdict

sizeA, sizeB = map(int, input().split())
stringA = defaultdict(lambda: [])
for i in range(sizeA):
    char = input()
    stringA[char].append(i + 1)
for i in range(sizeB):
    char = input()
    if len(stringA[char]) != 0:
        print(*stringA[char], sep=" ")
    else:
        print(-1)




