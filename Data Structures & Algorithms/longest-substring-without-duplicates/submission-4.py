class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        l = 0
        longest = 0

        for i in range(len(s)):
            if s[i] in letters:
                l = max(letters[s[i]] + 1, l)
            letters[s[i]] = i
            longest = max(longest, i - l + 1)
        
        return longest


            







        