def designPdfViewer(arr, string):
    lenOfCharacters = [0] * len(string)
    for index in range(len(string)):
        lenOfCharacters[index] = arr[ord(string[index]) - 97]
    highest = lenOfCharacters[0]
    for lenChar in lenOfCharacters:
        if lenChar > highest:
            highest = lenChar
    return len(string) * highest


arrayHeight = [int(i) for i in input().split()]
word = input()
print(designPdfViewer(arrayHeight, word))


