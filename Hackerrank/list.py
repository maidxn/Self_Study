commands = int(input())
arr = []
for each in range(commands):
    new_command = input()
    if 'insert' in new_command:
        new_command = new_command.split()
        arr.insert(int(new_command[1]), int(new_command[2]))
    elif 'print' in new_command:
        print(arr)
    elif 'remove' in new_command:
        new_command = new_command.split()
        arr.remove(int(new_command[1]))
    elif 'append' in new_command:
        new_command = new_command.split()
        arr.append(int(new_command[1]))
    elif 'sort' in new_command:
        arr.sort()
    elif 'pop' in new_command:
        arr.pop()
    else:
        arr.reverse()
