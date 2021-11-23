days = int(input())
liked = 2
people = 5
for i in range(2, days + 1):
    people = people // 2 * 3
    # print("PEOPLE", people)
    liked += people // 2
    # print("LIKE", liked)
print(liked)
