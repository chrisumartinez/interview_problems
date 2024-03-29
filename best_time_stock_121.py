# #LEETCODE PROBLEM: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is
# the price of a given stock on the ith day.

# You want to maximize your profit by choosing a
# single day to buy one stock and choosing a
# different day in the future to sell that stock.

# Return the maximum profit you can achieve
#  from this transaction. If you cannot achieve any profit, return 0.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and
# sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on
# day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions
# are done and the max profit = 0.


from typing import List


def maxProfit(prices: List[int]) -> int:

    # # insufficient data:
    # if len(prices) < 2:
    #     return 0

    # minimum = prices[0]
    # profit = 0
    # for i in range(1, len(prices)):
    #     # if prices[i] < minimum:
    #     #     minimum = prices[i]
    #     # else:
    #     minimum = min(minimum, prices[i])
    #     profit = max((prices[i] - minimum), profit)
    # return profit

    if len(prices) < 2:
        return 0

    minPrice = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        # if prices[i] is lower than min:
        if prices[i] < minPrice:
            minPrice = prices[i]
        else:
            profit = max((prices[i] - minPrice), profit)
    return profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Expected 5: 1 - 6 == 5

prices2 = [7, 6, 4, 3, 1]
print(maxProfit(prices2))  # Expected 0: No Profit
