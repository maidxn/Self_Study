class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if stack:
                    check = stack.pop()
                    if check == '(' and c == ')' or check == '[' and c == ']' or check == '{' and c == '}':
                        continue
                    else:
                        return False
                else:
                    return False
        return True if not stack else False