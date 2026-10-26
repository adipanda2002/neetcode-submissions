class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer = 0
        rightPointer = len(numbers) - 1

        while leftPointer < rightPointer:
            sum = numbers[leftPointer] + numbers[rightPointer]
            if sum == target:
                return [leftPointer + 1, rightPointer + 1]
            if sum > target:
                rightPointer -= 1
            else:
                leftPointer += 1