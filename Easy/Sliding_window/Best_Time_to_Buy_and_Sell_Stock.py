"""
Memory: O(1)
Time: O(N   )
"""
class Solution:
    def maxProfit(self, prices):
        #left = buy || right = sell
        l, r = 0, 1
        maxP = 0

        # Keep iterating through prices whilst the right pointer
        # has not passed the end of prices
        while r < len(prices):
            # Check whether its profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # Compare maxP and current profit
                maxP = max(maxP, profit)
            else:
                # If not shift it all the way to the right because
                # we've found the lowest price possible
                l = r
            # Regardless of the circumstances we need to upgrade the right pointer
            r += 1
        return maxP

        