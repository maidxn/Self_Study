class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        cur_value = 1
        while left <= right:
            for i in range(left, right + 1):
                matrix[top][i] = cur_value
                cur_value += 1
            top += 1
            
            for i in range(top, bottom + 1):
                matrix[i][right] = cur_value
                cur_value += 1
            right -= 1
            
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = cur_value
                cur_value += 1
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = cur_value
                cur_value += 1
            left += 1
        return matrix