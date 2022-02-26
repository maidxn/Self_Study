string = input()
ans = ''
for pos in range(len(string)):
    add = string[pos]
    if (pos == 0 or string[pos - 1] == ' ') and 97 <= ord(string[pos]) <= 122:
        add = chr(ord(string[pos]) - 32)
    ans += add
print(ans)

