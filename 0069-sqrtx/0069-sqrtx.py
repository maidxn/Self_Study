class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        while (res + 1) * (res + 1) <= x:
            res += 1
        return res