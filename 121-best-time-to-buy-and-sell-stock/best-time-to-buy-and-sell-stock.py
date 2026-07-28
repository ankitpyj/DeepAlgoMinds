class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for curr in prices:
            min_price = min(curr,min_price)
            profit = curr -min_price
            max_profit = max(profit ,max_profit)

        return max_profit