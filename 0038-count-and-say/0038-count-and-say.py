class Solution:
    def countAndSay(self, n: int) -> str:
        
        def countFunction(s):
            res = ""
            count = 1
            for index in range(len(s)):
                if index == len(s) - 1 or s[index] != s[index + 1]:
                    res += str(count) + s[index]
                    count = 1
                else:
                    count += 1
            return res
        
        ans = "1"
        for i in range(2, n+1):
            ans = countFunction(ans)
        return ans
        
        