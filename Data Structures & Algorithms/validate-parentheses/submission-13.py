class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")" : "(", "]": "[", "}": "{"}
        stack = []

        for bracket in s:
            if bracket in brackets:
                if not stack:
                    return False
                if stack[-1] != brackets[bracket]:
                    return False
                stack.pop(-1)
                continue
            stack.append(bracket)

        return True if not stack else False
            

        