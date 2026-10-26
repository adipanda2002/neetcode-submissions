class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        seen = {}

        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        
        for char in t:
            if char not in seen or seen[char] == 0:
                return False
            seen[char] -= 1
        
        return True

