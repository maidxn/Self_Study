class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7

        # Sum for complete weeks:
        # Each week adds (28 + 7 * i), where i is week index starting from 0
        total = 28 * weeks + 7 * (weeks * (weeks - 1)) // 2

        # Sum for remaining days (arithmetic sequence)
        total += days * (weeks + 1) + (days * (days - 1)) // 2

        return total
        