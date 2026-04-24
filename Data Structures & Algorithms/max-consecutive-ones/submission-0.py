class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0: # no longer consecutive
                count = 0
            else:
                count += 1
            maxNum = max(maxNum, count)
        return maxNum