class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            prefix, postfix = 1, 1
            if i == 0:
                prefix = 1
            else:
                for n in range(i):
                    prefix *= nums[n]
            
            if i == len(nums) - 1:
                postfix = 1
            else:
                for n in range(i + 1, len(nums)):
                    postfix *= nums[n]
            
            res.append(prefix * postfix)
        
        return res
            

