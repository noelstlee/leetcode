class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = defaultdict(int)

        for index, num in enumerate(nums):
            diff = target - num
            if diff in numMap:
                return [numMap[diff], index]
            numMap[num] = index