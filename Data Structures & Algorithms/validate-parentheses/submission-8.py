class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {')': '(', '}': '{', ']': '['}
        stack = []

        for bracket in s:
            if bracket in mappings:
                if stack and mappings[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return True if not stack else False
