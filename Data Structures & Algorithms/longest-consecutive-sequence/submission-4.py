class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        res = []
        maxLength = 0

        for num in nums:
            numSet.add(num)
        
        for num in nums:
            res.clear()
            res.append(num)
            if num - 1 not in numSet: # run while loop only when num is first
                while num + 1 in numSet:
                    res.append(num + 1)
                    num = num + 1
            else:
                continue
            maxLength = max(maxLength, len(res))
        
        return maxLength
