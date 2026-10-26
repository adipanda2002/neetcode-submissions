class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minimumPrice = prices[0]

        for price in prices:
            minimumPrice = min(minimumPrice, price)
            maxProfit = max(maxProfit, price - minimumPrice)

        return maxProfit
        