class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0 
        maxSum = nums[0]

        for num in nums:
            curSum = max(curSum, 0) # check if curSum is negative, if so we set to 0
            curSum += num
            maxSum = max(curSum, maxSum) # store the maxSum
        return maxSum
