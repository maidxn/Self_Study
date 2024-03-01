class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1): 
            for c in range(n-2, -1, -1):
                row[c] = row[c+1] + row[c]
        return row[0]