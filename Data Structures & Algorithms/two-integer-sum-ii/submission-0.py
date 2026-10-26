class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer = 0
        rightPointer = len(numbers) - 1

        while True:
            if numbers[leftPointer] + numbers[rightPointer] == target:
                return [leftPointer + 1, rightPointer + 1]
            if numbers[leftPointer] + numbers[rightPointer] > target:
                rightPointer -= 1
            else:
                leftPointer += 1