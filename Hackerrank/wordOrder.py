from collections import Counter

words = int(input())
dictionary = {}
for word in range(words):
    new = input()
    if new not in dictionary.keys():
        dictionary[new] = 1
    else:
        dictionary[new] += 1
print(len(dictionary))
print(*dictionary.values(), sep=' ')

# Second way, anyway, the counter is super usefullll
arr = []
for word in range(words):
    arr.append(input())
counter = Counter(arr)
print(len(counter))
print(*counter.values(), sep=' ')
