from collections import Counter
string = input()
split = int(input())
indices = list(map(lambda x: x * split, range(len(string)//split)))
substring = [string[i:i+split] for i in indices]
for each in substring:
    print(*Counter(each), sep='')
