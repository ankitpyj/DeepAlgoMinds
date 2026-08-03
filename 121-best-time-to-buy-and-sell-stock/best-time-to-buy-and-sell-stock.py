class Solution(object):
    def maxProfit(self, prices):
        
        mini = prices[0]
        max_profit = 0

        for curr in prices:
            mini = min(curr,mini)
            profit = curr - mini

            max_profit = max(max_profit,profit)

        return max_profit
        