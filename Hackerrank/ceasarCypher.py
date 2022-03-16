stringLengh = int(input())
string = input()
shift = int(input()) % 26

# This is how to do if I follow the normal steps to make Ceasar cypher
# And don't remember ascii codes of alphabets :>
new_start = ord('a') + shift
newAlphabet = list(range(new_start, ord('z') + 1))
alphabet = list(range(ord('a'), ord('z') + 1))
add = ord('a')

while len(newAlphabet) < 26:
    newAlphabet.append(add)
    add += 1

ans = ''
for char in string:
    if ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z'):
        code = ord(char) + 32 if ord(char) < 97 else ord(char)
        isUpper = True if ord(char) < 97 else False
        index = alphabet.index(code)
        ans = ans + chr(newAlphabet[index]) if not isUpper else ans + chr(newAlphabet[index]).upper()
    else:
        ans += char
print(ans)


# Another way to do is more simple
stringCode = [ord(x) for x in string]
for index in range(stringLengh):
    if 65 <= stringCode[index] <= 90:
        stringCode[index] = 65 + ((stringCode[index] - 65) + shift) % 26
        # stringCode[index] - 65 + shift => to get the new position
        # % 26, to adjust if the position after adding has value > 26
        # + 65 to sure that is will start with a (or A in the situation below)
    elif 97 <= stringCode[index] <= 122:
        stringCode[index] = 97 + ((stringCode[index] - 97) + shift) % 26
newString = [chr(i) for i in stringCode]
print(''.join(newString))
