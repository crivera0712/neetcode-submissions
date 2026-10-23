class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we are given a list of ints, where prices[i] represents the price
        # of a stock on the ith day. we can choose a single day to buy a stock
        # and a different day in the future to sell the stock 
        # return the max profit, we can choose to make no transactions 
        # resulting in a 0 profit 

        left, right = 0,0 
        profit = 0 

        while right < len(prices):
            profit = max(profit, prices[right] - prices[left])
            if (prices[right] < prices[left]):
                left = right
            right += 1

        return profit
        