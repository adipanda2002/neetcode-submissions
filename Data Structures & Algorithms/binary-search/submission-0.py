class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            i = (start + end) // 2
            if nums[i] < target:
                start = i + 1
            elif nums[i] > target:
                end = i
            elif nums[i] == target:
                return i

            if start == end and nums[start] != target:
                return -1