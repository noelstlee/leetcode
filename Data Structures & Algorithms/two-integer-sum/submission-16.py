class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} # number : index
        index = 0
        for num in nums:
            numMap[num] = index
            index += 1
        
        for i in range(len(nums)):
            if target - nums[i] in numMap and numMap[target - nums[i]] != i:
                return [i, numMap[target - nums[i]]]