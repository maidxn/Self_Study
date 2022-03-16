sizeA = int(input())
setA = set(map(int, input().split()))
sizeB = int(input())
setB = set(map(int, input().split()))
ans = set()
ans = ans.union(setA.difference(setB), setB.difference(setA))
print(*sorted(ans), sep='\n')



