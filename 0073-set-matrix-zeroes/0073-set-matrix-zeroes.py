class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indices = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    indices.append([i, j])
        for index in indices:
            for r in range(len(matrix)):
                for c in range(len(matrix[0])):
                    if r == index[0] or c == index[1]:
                        matrix[r][c] = 0
        
        