class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for letter in s:
            if letter not in seen:
                seen[letter] = 1
                continue
            seen[letter] += 1
        
        for letter in t:
            if letter not in seen:
                return False
            seen[letter] -= 1
            if seen[letter] < 0:
                return False

        for value in seen.values():
            if value != 0:
                return False
        
        return True
        