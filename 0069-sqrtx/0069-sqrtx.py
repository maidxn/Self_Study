class Solution:
    def mySqrt(self, x: int) -> int:
        # res = 0
        # while (res + 1) * (res + 1) <= x:
        #     res += 1
        # return res
    
        # binary search
        left, right = 0, x
        while left <= right:
            mid = (right + left) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right