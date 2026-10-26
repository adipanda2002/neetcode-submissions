class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = {}
        for item in nums:
            if item not in tracker:
                tracker[item] = True
                continue
            else:
                return True
        return False
            

            
            

         