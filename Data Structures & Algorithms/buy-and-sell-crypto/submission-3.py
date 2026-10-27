class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestEntry = float('inf')

        for i, price in enumerate(prices):
            if i == 0:
                lowestEntry = price
                continue
            
            if price < prices[i - 1]:
                maxProfit = max(maxProfit, prices[i - 1] - lowestEntry)
                lowestEntry = min(price, lowestEntry)

            maxProfit = max(maxProfit, prices[i] - lowestEntry)

        return maxProfit



        