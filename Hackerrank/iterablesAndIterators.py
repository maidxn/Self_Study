from itertools import combinations

size = int(input())
string = input()
string = string.replace(' ', '')
k = int(input())
com = list(combinations(string, k))

# Mai's way
count = 0
for each in com:
    if 'a' in each:
        count += 1
print(count/len(com))

# Or another way
have_A = list(filter(lambda each: 'a' in each, com))
print(len(have_A)/len(com))
