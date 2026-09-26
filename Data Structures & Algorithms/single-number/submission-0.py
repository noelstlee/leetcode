class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a ^ a = 0
        # a ^ 0 = a
        res = 0
        for num in nums:
            res = num ^ res

        return res