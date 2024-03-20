class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows <= 1:
            return [[1]]
        res.append([1])
        for i in range(2, numRows + 1):
            row = [0] * i
            row[0], row[-1] = 1, 1
            if i - 1 == 1:
                res.append(row)
                continue
            pre_row = res[i - 2]
            for index in range(1, i - 1):
                row[index] = pre_row[index - 1] + pre_row[index]
            res.append(row)
        return res