class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in range(0, len(nums)):
            num = nums[i]
            if num not in seen:
                seen[num] = 1
                continue
            seen[num] += 1
            if seen[num] > 1:
                return True
            else:
                seen[num] += 1
        return False
    


        