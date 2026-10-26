class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            alphabet = [0] * 26
            for letter in string:
                index = ord(letter) - ord('a')
                alphabet[index] += 1
            key = tuple(alphabet)
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
        
        return [anagrams[i] for i in anagrams]