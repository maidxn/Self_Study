class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stack_asterisk = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                stack_asterisk.append(i)
            else:
                if stack:
                    stack.pop()
                elif stack_asterisk:
                    stack_asterisk.pop()
                else:
                    return False
        while stack and stack_asterisk:
            if stack[-1] < stack_asterisk[-1]:
                stack.pop()
                stack_asterisk.pop()
            else:
                return False
        return len(stack) == 0