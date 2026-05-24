class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set() # use this to O(1) search for consecutive elements
        res, count = 0, 0 # return value of total consecutive nums

        # setup the check set to find all elements
        for num in nums:
            check.add(num)
        
        for num in nums:
            count = 1
            while num + 1 in check:
                count += 1
                num += 1
            res = max(res, count)

        return res