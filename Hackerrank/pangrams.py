string = input()
string = string.lower()
string = string.replace(' ', '')

alphabet = {}
for char in string:
    if char not in alphabet.keys():
        alphabet[char] = 1
    else:
        alphabet[char] += 1

# Another way to code. 5 -> 2 lines
for char in string:
    alphabet[char] = 1 if char not in alphabet.keys() else alphabet[char] + 1

print("pangram" if len(alphabet.keys()) == 26 else "not pangram")
