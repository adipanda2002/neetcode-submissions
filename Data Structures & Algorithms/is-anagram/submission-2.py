class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_chars = {}
        t_chars = {}

        for i in range(len(s)):
            update(s_chars, s[i])
            update(t_chars, t[i])

        for key in s_chars:
            if key not in t_chars:
               return False
            if s_chars[key] != t_chars[key]:
                return False

        return True

    
def update(table, key):
    if key in table:
        table[key] += 1
    else:
        table[key] = 0   