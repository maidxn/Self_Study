string = input()
dictionary = {}

for char in string:
    if char not in dictionary.keys():
        dictionary[char] = 1
    else:
        dictionary[char] += 1

odd = 0
ans = "YES"
for key in dictionary.keys():
    if dictionary[key] % 2 != 0:
        odd += 1
        ans = "NO" if odd > 1 else "YES"
print(ans)

