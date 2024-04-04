class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack or c != pairs[stack.pop()]:
                    return False
        return True if not stack else False