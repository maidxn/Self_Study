size = int(input())
scores = [int(i) for i in input().split()]

first, second = -100, -100

for score in scores:
    if score > first:
        second = first
        first = score
    elif score > second and score != first:
        second = score

print(second)
