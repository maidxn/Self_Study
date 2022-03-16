from collections import Counter


arrSize, setSize = map(int, input().split())
arr = Counter(map(int, input().split()))
like = set(map(int, input().split()))
dislike = set(map(int, input().split()))
happiness = 0

for each in like:
    if each in arr.keys():
        happiness += arr[each]
for each in dislike:
    if each in arr.keys():
        happiness -= arr[each]
print(happiness)

# Another way to do, it is easier to understand here
C = like.union(dislike)
arr = [i for i in arr if i in C]
print(sum(1 if i in like else -1 for i in arr))

# The solution is here
print(sum([(i in like) - (i in dislike) for i in arr]))
# It says that i in like ~ with like.count(i) :O
# Oh whao, I didn't know that








