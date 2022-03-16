string = input()
index, char = input().split()

listOfString = list(string)
listOfString[int(index)] = char
string = ''.join(listOfString)
print(string)
