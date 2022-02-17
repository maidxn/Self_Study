import re


# My way
def FindHackerRank(string):
    pos = 0
    count = 0
    standard = "hackerrank"
    for char in string:
        if count == len(standard):
            break
        if standard[pos] == char:
            pos += 1
            count += 1
    ans = "YES" if count == len(standard) else "NO"
    return ans


numberOfStrings = int(input())
for each in range(numberOfStrings):
    print(FindHackerRank(input()))


# I found this way to, it's just two line
for each in range(int(input())):
    print("YES" if re.search('.*'.join("hackerrank"), input()) else "NO")

# . = any character, * = zero or more characters
# Yeah, I know, it's really uhm "gợi đòn, thiếu đánh, đáng khinh" but it's so cool
