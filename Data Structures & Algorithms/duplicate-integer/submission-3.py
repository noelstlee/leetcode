class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate through list and check for duplicate
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
            