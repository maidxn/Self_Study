class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins = 1
        total = 0
        rows = 0
        while total + coins <= n:
            total += coins
            coins += 1
            rows += 1
        return rows
        