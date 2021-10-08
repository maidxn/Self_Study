def CheckGreater(r, c, array2D):
    if array2D[r][c] > array2D[r - 1][c] and array2D[r][c] > array2D[r + 1][c] and array2D[r][c] > array2D[r][c - 1] and array2D[r][c] > array2D[r][c + 1]:
        return True
    return False


gridSize = int(input())
matrix = []
for index in range(gridSize):
    temp = input()
    row = []
    for item in temp:
        row.append(int(item))
    matrix.append(row)

ans = []
for rowIndex in range(1, gridSize - 1):
    for columnIndex in range(1, gridSize - 1):
        if CheckGreater(rowIndex, columnIndex, matrix):
            ans.append((rowIndex, columnIndex))

for change in range(len(ans)):
    indices = ans[change]
    matrix[indices[0]][indices[1]] = "X"

for index in range(gridSize):
    print(*matrix[index], sep='')
