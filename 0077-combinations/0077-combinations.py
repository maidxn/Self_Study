class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtracking(index, combination):
            if len(combination) == k:
                res.append(combination[:])
                return
            for i in range(index, n + 1):
                combination.append(i)
                backtracking(i + 1, combination)
                combination.pop()
        backtracking(1, [])
        return res