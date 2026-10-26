class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num,0)
        
        return sorted(counts, key=lambda x: counts[x], reverse=True)[:k]
        