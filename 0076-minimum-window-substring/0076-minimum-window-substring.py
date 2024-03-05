class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapT, window = {}, {}
        
        for c in t:
            mapT[c] = 1 + mapT.get(c, 0)
        
        left = 0
        charsWindow, charsT = 0, len(mapT)
        res, minLength = [-1, -1], float("inf")
        
        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)
            
            if s[right] in mapT and mapT[s[right]] == window[s[right]]:
                charsWindow += 1
            
            while charsWindow == charsT:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    res = [left, right]
                window[s[left]] -= 1
                if s[left] in mapT and window[s[left]] < mapT[s[left]]:
                    charsWindow -= 1
                left += 1
        return s[res[0]:res[1] + 1]
                
                