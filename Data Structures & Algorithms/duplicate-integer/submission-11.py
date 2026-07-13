class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupCheck = set()
        for n in nums:
            dupCheck.add(n)
        return False if len(dupCheck) == len(nums) else True
        