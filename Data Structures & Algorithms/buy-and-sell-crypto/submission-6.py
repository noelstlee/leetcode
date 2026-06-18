class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0

        for R in range(1, len(prices)):
            if prices[L] < prices[R]:
                profit = max(prices[R] - prices[L], profit)
            else:
                L = R
        
        return profit
