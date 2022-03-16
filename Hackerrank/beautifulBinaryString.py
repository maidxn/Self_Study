import re


lengh = int(input())
string = input()

substrings = re.finditer("010", string)
pos = [sub.start() for sub in substrings]
print(len(pos))

# https://www.kite.com/python/answers/how-to-find-the-indices-of-all-occurrences-of-a-substring-within-a-string-in-python

