# Welcome to GitHub Desktop!

This is your README. READMEs are where you can communicate what your project is and how to use it.

Write your name on line 6, save it, and then head back to GitHub Desktop.
TWO SUM
class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit
        
