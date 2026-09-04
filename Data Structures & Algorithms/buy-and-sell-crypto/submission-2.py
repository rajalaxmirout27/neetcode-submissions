class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # optimal approach

        buy = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                max_profit = max(profit, max_profit)

        return max_profit