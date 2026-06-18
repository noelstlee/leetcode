class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        profit = 0

        for i in range(len(prices) - 1):
            for j in range(i, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        
        return profit


