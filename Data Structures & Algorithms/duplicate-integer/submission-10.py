class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupCheck = set()
        for num in nums:
            if num in dupCheck:
                return True
            else:
                dupCheck.add(num)
        return False
