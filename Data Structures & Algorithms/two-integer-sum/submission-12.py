class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumMap = defaultdict() # key: num value (element) of nums array, value: index
        for i in range(len(nums)):
            if target - nums[i] in twoSumMap:
                index = twoSumMap.get(target - nums[i])
                return [index, i]
            else:
                twoSumMap[nums[i]] = i
        return None