class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dupeCheck = defaultdict(int)
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            target = nums[i]
            L = i + 1
            R = len(nums) - 1
            while L < R:
                if nums[L] + nums[R] > -target:
                    R -= 1
                elif nums[L] + nums[R] < -target:
                    L += 1
                else:
                    dupeCheck[(nums[i], nums[L], nums[R])] += 1
                    if dupeCheck[(nums[i], nums[L], nums[R])] == 1:
                        res.append([nums[i], nums[L], nums[R]])
                    L += 1
        return res
