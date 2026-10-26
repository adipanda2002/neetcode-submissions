class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        res = end

        while start <= end:
            k = (start + end) // 2  
            totalTime = 0   
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <= h:
                res = k
                end = k - 1
            else:
                start = k + 1
        return res