class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")" : "(", "]": "[", "}": "{"}
        tracker = []

        for bracket in s:
            if bracket in brackets:
                if not tracker:
                    return False
                if tracker[-1] != brackets[bracket]:
                    return False
                tracker.pop(-1)
                continue
            tracker.append(bracket)

        return True if not tracker else False
            

        