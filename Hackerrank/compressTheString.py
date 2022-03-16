from itertools import groupby


print(*[(len(list(count)), int(i)) for i, count in groupby(input())], sep=" ")

# :) 2 lines, great.
# Groupby means, if there are many objects similar and next to each others
# It will become a group. Not like count all occurrences, ok?


