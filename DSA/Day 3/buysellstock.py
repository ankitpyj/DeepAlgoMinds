def maxProfit(prices):

    min_price = prices[0]
    max_profit = 0

    for curr_price in prices:

        min_price = min(min_price,curr_price)

        profit = curr_price - min_price

        max_profit = max(max_profit,profit)
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))