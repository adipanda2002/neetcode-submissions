class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # if a > 0:
            #     break

            if i > 0 and a == nums[i - 1]:
                continue

            leftPointer, rightPointer = i + 1, len(nums) - 1
            while leftPointer < rightPointer:
                threeSum = a + nums[leftPointer] + nums[rightPointer]
                if threeSum > 0:
                    rightPointer -= 1
                elif threeSum < 0:
                    leftPointer += 1
                else:
                    res.append([a, nums[leftPointer], nums[rightPointer]])
                    leftPointer += 1
                    rightPointer -= 1
                    while nums[leftPointer] == nums[leftPointer - 1] and leftPointer < rightPointer:
                        leftPointer += 1
        return res  

