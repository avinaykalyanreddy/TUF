"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

prices = [7,1,5,3,6,4]


min_val = float("inf")

res = 0

for i in prices:

    if i < min_val:

        min_val = i
    else:

        res = max(res,i - min_val)

print(res)