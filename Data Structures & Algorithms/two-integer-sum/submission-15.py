class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numTarget = {}
        index = 0
        
        for i in range(len(nums)):
            numTarget[nums[i]] = i # num: index

        for i in range(len(nums)):
            if target - nums[i] in numTarget and numTarget[target - nums[i]] != i:
                return [i, numTarget[target - nums[i]]]
            