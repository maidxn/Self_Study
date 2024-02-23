class Solution:
    def reverse(self, x: int) -> int:
    
        negative = True if x < 0 else False
        x = abs(x)
        res = 0
        while x > 0:
            digit = x % 10
            res = res * 10 + digit
            x = x // 10
        res = res if res.bit_length() < 32 else 0
        return res if not negative else -res
            
        
        