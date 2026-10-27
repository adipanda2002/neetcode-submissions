class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestEntry = prices[0]

        for sell in prices:
            maxProfit = max(maxProfit, sell - lowestEntry)
            lowestEntry = min(lowestEntry, sell)
        return maxProfit



        