class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupCheck = set()
        for num in nums:
            if num in dupCheck:
                return True
            dupCheck.add(num)
        return False