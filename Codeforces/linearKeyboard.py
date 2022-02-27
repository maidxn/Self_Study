def CalculateTime(keyboard, s):
    indices = [keyboard.index(char) for char in s]
    res = 0
    for index in range(1, len(indices)):
        res += abs(indices[index] - indices[index - 1])
    return res


testCases = int(input())
for testCase in range(testCases):
    alphabet = input()
    string = input()
    print(CalculateTime(alphabet, string))



