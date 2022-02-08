def ConvertToPalindrome(query):
    start = 0
    end = len(query) - 1
    numOfOperations = 0
    while start <= end:
        numOfOperations += abs(ord(query[start]) - ord(query[end]))
        start += 1
        end -= 1
    print(numOfOperations)


numberOfQuery = int(input())
for each_q in range(numberOfQuery):
    q = input()
    ConvertToPalindrome(q)
