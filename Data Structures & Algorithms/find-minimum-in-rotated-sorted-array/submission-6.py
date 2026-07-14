class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if rotated:
        if nums[len(nums) - 1] < nums[0]:
            low, high = 0, len(nums) - 1
            res = nums[low]
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= nums[0]: # mid is in larger subset
                    low = mid + 1
                else:
                    high = mid - 1
                res = min(nums[mid], res)
            return res
        # not rotated:
        else:
            return nums[0]