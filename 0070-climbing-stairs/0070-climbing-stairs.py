class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        # dp
        # dp = [0] * n
        # dp[0], dp[1] = 1, 2
        # for i in range(2, n, 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[-1]
        
        # no dp
        pre1, pre2 = 1, 2
        for i in range(2, n, 1):
            current = pre1 + pre2
            pre1 = pre2
            pre2 = current
        return current