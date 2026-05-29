class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        length = float("inf")
        windowSum = 0

        for R in range(len(nums)):
            windowSum += nums[R]
            while windowSum >= target: # keep on shortening the window when condition meets to find minimum length
                length = min(length, R - L + 1)
                windowSum -= nums[L]
                L += 1
        return 0 if length == float("inf") else length