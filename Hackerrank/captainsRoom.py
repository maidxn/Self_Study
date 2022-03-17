from collections import Counter


group = int(input())
print(Counter(map(int, input().split())).most_common()[-1][0])
# Yeah, BIF helps alot
# But the solution here is using mathematic so ehh
K = int(input())
set_S = set()
sumlist_S = 0
for i in input().split():
    I = int(i)
    set_S.add(I)
    sumlist_S += I
print((sum(set_S)*K - sumlist_S)//(K-1))
