def AlternatingCharacters(s):
    countDeletion, pos = 0, 0
    while pos < len(s) - 1:
        if s[pos] == s[pos + 1]:
            countDeletion += 1
        pos += 1
    return countDeletion


numberOfTestcase = int(input())

for testcase in range(numberOfTestcase):
    string = input()
    print(AlternatingCharacters(string))
