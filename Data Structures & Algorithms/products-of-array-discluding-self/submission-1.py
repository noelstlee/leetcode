class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        prod = 1
        out = []
        l_prod = 1
        r_prod = 1

        for i in range(1, len(nums)):
            prod *= nums[i]
        
        out.append(prod)
        prod = 1
        
        for i in range(1, len(nums) - 1):
            left = nums[:i]
            right = nums[i + 1:len(nums)]
            if len(left) != 0:
                for num in left:
                    l_prod *= num
            if len(right) != 0:
                for num in right:
                    r_prod *= num
            prod = l_prod * r_prod
            # add to out
            out.append(prod)
            # reset
            left.clear()
            right.clear()
            l_prod = 1
            r_prod = 1
            prod = 1

        for i in range(len(nums) - 1):
            prod *= nums[i]
        out.append(prod)

        return out
            