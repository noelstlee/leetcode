class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit means (max selling price) - (min purchase price)
        # condition: min purchase price's date < max selling price's date
        profit = 0
        L = 0

        for R in range(1, len(prices)):
            print(f"{profit}: [{L}, {R}] -> {prices[R] - prices[L]}")
            if prices[L] < prices[R]:
                profit = max(profit, prices[R] - prices[L])
            else:
                L = R
        return profit