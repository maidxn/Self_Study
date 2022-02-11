from collections import Counter

size = int(input())

arr = list(map(int, input().split()))

# First way
arr = sorted(arr)
ans = -1

if size == 1:
    ans = size
else:
    for index in range(0, size):
        if index == 0:
            ans = arr[index] if arr[index] != arr[index + 1] else -1
        elif index == size - 1:
            ans = arr[index] if arr[index] != arr[index - 1] else -1
        elif arr[index] != arr[index + 1] and arr[index] != arr[index - 1]:
            ans = arr[index]
            break

print(ans)

# Second way
counter = Counter(arr)
for each in counter:
    if counter[each] == 1:
        print(each)
        break


