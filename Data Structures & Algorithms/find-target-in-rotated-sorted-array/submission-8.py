class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
    
        while L <= R:
            M = (L + R) // 2
            if nums[M] > target: # too big
                if nums[M] >= nums[L]: # left portion of sorted array (big leagues)
                    if nums[L] > target: # even the smallest one in the big leagues exceed target, go to small league
                        L = M + 1
                    else: # target can be found in this portion, do binary search
                        R = M - 1
                else:
                    R = M - 1
            elif nums[M] < target: # too small
                if nums[M] < nums[L]: # left portion of sorted array (small leagues)
                    if nums[R] < target: # even the largest one in the big leagues is smaller than target, go to the big leagues
                        R = M - 1
                    else: # target can be found in this portion do binary search
                        L = M + 1
                else:
                    L = M + 1
            else: # same
                return M
        return -1