class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i in brackets:
                if stack and brackets[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False
