size = int(input())
arr = set(map(int, input().split()))
numberOfCommands = int(input())

for command in range(numberOfCommands):
    userInput = input()
    if userInput == "pop":
        arr.pop()
    else:
        execute, number = userInput.split()
        if execute == 'discard':
            arr.discard(int(number))
        else:
            arr.remove(int(number))
print(sum(arr))
