numberOfChapter, maxProblems = map(int, input().split())
arrayProblems = [int(i) for i in input().split()]
page = 1
specificProblems = 0

for chapterIndex in range(1, numberOfChapter + 1):
    # print("The chapter's problems", arrayProblems[chapterIndex - 1])
    pageCost = arrayProblems[chapterIndex - 1] // maxProblems
    # print("Page cost", pageCost)
    start = 1
    end = maxProblems + 1
    end = maxProblems + 1 if pageCost != 0 else arrayProblems[chapterIndex - 1] + 1
    pageCost = 1 if pageCost == 0 else pageCost
    pageCost = pageCost + 1 if pageCost * maxProblems < arrayProblems[chapterIndex - 1] else pageCost
    # print("Page cost change", pageCost)
    for eachPage in range(1, pageCost + 1):
        # print("The page now", page)
        # print("S - E", start, end)
        if page in range(start, end):
            specificProblems += 1
            # print("Increase", specificProblems)
        start = end
        # It takes me an hour to realize that it's <= not just <. Seriously????
        end = end + maxProblems if end + maxProblems <= arrayProblems[chapterIndex - 1] else arrayProblems[chapterIndex - 1] + 1
        page += 1

print(specificProblems)


