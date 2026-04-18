class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate through list and check for duplicate
        nums.sort() # O(nlogn)
        for i in range(len(nums) - 1): # O(n)
            if nums[i] == nums[i + 1]:
                return True
        return False
            # time complexity O(nlogn), since sorting dominates time complexity