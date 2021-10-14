string = input()
words = 1
for char in string:
    if ord(char) < 97:
        words += 1
print(words)
