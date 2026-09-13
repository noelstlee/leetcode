class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexStorage = {} # keys: number, value: index
        i = 0
        for num in nums:
            indexStorage[num] = i
            i += 1
        
        for i in range(len(nums)):
            if target - nums[i] in indexStorage and i != indexStorage[target - nums[i]]:
                return [i, indexStorage[target - nums[i]]]
