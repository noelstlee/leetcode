class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            # if exceed window limit:
            if R - L > k:
                window.discard(nums[L])
                L += 1
            # check duplicate
            if nums[R] in window:
                return True
            window.add(nums[R]) # add element to hash set "window"
        return False