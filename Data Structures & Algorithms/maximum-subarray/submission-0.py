class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        # not needing to iterate O(n^2) times instead O(n)
        cumSum = float("-inf")
        maxSum = float("-inf")

        for i in range(len(nums)):
            cumSum = max(0, cumSum)
            cumSum += nums[i]
            maxSum = max(maxSum, cumSum)
        return maxSum
