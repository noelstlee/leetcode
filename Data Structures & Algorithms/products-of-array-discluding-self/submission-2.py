class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            frontProd = 1
            postProd = 1
            for f in range(0, i):
                frontProd *= nums[f]
            for p in range(i + 1, len(nums)):
                postProd *= nums[p]
            res.append(frontProd * postProd)
        
        return res