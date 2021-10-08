def CountA(start, end, string):
    c = 0
    for i in range(start, end):
        if string[i] == 'a':
            c += 1
    return c


String = input()
location = int(input())

index = location % (len(String))
times = location // len(String)
count = CountA(0, len(String), String)
last = CountA(0, index, String)

print(times * count + last)

