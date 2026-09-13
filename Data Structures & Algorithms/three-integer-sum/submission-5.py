class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        dupCheck = set()
        nums.sort()
        for i in range(len(nums) - 2):
            L, R = i + 1, len(nums) - 1
            target = nums[i]
            while L < R:
                if nums[L] + nums[R] == -nums[i]:
                    if (target, nums[L], nums[R]) not in dupCheck:
                        res.append([target, nums[L], nums[R]])
                        dupCheck.add((target, nums[L], nums[R]))
                    L += 1
                    R -= 1
                elif nums[L] + nums[R] < -nums[i]:
                    L += 1
                else:
                    R -= 1
        return res