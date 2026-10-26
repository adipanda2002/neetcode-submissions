import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum = math.inf

        for price in prices:
            if price < minimum:
                minimum = price
            profit_at_price = price - minimum
            if profit_at_price > max_profit:
                max_profit = profit_at_price

        return max_profit

        