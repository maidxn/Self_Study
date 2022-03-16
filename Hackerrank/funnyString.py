def FunnyString(s):
    diffArray = []
    for pos in range(1, len(s)):
        diffArray.append(abs(ord(s[pos]) - ord(s[pos - 1])))
    reversedString = s[::-1]
    for pos in range(1, len(reversedString)):
        if abs(ord(reversedString[pos]) - ord(reversedString[pos - 1])) != diffArray[pos - 1]:
            return "Not Funny"
    return "Funny"


numberOfTestcase = int(input())
for testcase in range(numberOfTestcase):
    string = input()
    print(FunnyString(string))
