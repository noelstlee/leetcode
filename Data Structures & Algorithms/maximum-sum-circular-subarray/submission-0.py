class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = 0
        global_max = nums[0]
        cur_min = 0
        global_min = nums[0]
        total = sum(nums)

        for num in nums:
            cur_max = max(num, cur_max + num)
            global_max = max(cur_max, global_max)
            cur_min = min(num, cur_min + num)
            global_min = min(cur_min, global_min)
        
        return max(total - global_min, global_max) if global_max > 0 else global_max