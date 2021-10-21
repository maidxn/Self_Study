size = int(input())
first, second = 0, 1
array = []
if size < 3:
    if size > 0:
        array = [0] if size == 1 else [0, 1]
else:
    array = [0, 1]
    for index in range(2, size):
        array.append(array[first] + array[second])
        first = second
        second += 1

cube = lambda number: pow(number, 3)
print(list(map(cube, array)))
