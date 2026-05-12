# problem explained at 3:22:00
# best time to buy and sell stocks to gain maximum profit
    
def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit_value = 0

    for price in prices:
        min_price = min(min_price, price)

        profit = price - min_price

        max_profit_value = max(max_profit_value, profit)

    return max_profit_value


# Example
# input: array of prices:
prices = [7, 1, 5, 3, 6, 4]
# price for day 1 : 7
# price for day 2 : 1
# price for day 3 : 5
# price for day 4 : 3
# price for day 5 : 6
# price for day 6 : 4


print(max_profit(prices))