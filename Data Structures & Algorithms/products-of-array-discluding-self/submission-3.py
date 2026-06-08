class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        front = [1] * len(nums)
        post = [1] * len(nums)
        fProd = 1
        pProd = 1

        for i in range(1, len(nums)):
            fProd *= nums[i - 1]
            front[i] = fProd
        
        print(front)
        
        for j in range(len(nums) - 2, -1, -1):
            pProd *= nums[j + 1]
            post[j] = pProd
        
        print(post)
        
        for k in range(len(nums)):
            res[k] = front[k] * post[k]
        
        return res
        