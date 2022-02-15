from collections import Counter
string = input()

# It will be the best way if the problem doesn't like this OSS <- still has the same
# number, but its order is wrong ;;;-;;

dictionary = Counter(string)
print(len(string) - dictionary['O'] - dictionary['S'])

# So the solution is
changed = 0
sosString = ['S', 'O', 'S']
pos = 0
for char in string:
    if char != sosString[pos]:
        changed += 1
    pos = pos + 1 if pos + 1 <= 2 else 0
print(changed)

# Another way, just 4 lines :>
# and this is where I found help
# https://stackoverflow.com/questions/16568056/nested-list-comprehension-with-two-lists
standardString = "SOS" * (len(string) // 3)
ans = [1 for x, y in zip(standardString, string) if x != y]
print(len(ans))
