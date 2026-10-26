class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = {}
        for num in nums:
            if num in tracker:
                if tracker[num] == True:
                    return True
            else:
                tracker[num] = True
        return False

                
         