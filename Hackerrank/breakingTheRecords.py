def breakingRecords(arr):
    highest_score = arr[0]
    lowest_score = arr[0]
    count_high = 0
    count_low = 0
    for score in arr:
        if score > highest_score:
            highest_score = score
            count_high += 1
        elif score < lowest_score:
            lowest_score = score
            count_low += 1
    return count_high, count_low


size = int(input())
scores = [int(i) for i in input().split()]

first, second = breakingRecords(scores)
print(first, second)



