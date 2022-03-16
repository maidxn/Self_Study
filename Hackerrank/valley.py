def CountingValleys(number, string):
    count = 0
    pos = 0
    for char in string:
        if char == 'U':
            pos += 1
        else:
            pos -= 1
        if pos == 0 and char == 'U':
            count += 1
    return count


steps = int(input())
path = input()
print(CountingValleys(steps, path))
