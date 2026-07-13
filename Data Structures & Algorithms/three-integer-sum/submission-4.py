class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dupCheck = set()
        res = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            target = -nums[i]
            L = i + 1
            R = len(nums) - 1
            while L < R:
                if nums[L] + nums[R] == target:
                    if (nums[i], nums[L], nums[R]) not in dupCheck:
                        dupCheck.add((nums[i], nums[L], nums[R]))
                    L += 1
                    R -= 1
                elif nums[L] + nums[R] < target:
                    L += 1
                else:
                    R -= 1
        for triplet in dupCheck:
            res.append(list(triplet))
        return res
