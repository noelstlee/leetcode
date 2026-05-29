class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        # count = 0
        # L = 0
        # window = []

        # for L in range(len(nums) - k + 1):
        #     windowSum = nums[L]
        #     window = []
        #     window.append(nums[L])
        #     for R in range(L + 1, min(len(nums), L + k)):
        #         windowSum += nums[R]
        #         window.append(nums[R])
        #     if (windowSum / k) >= threshold:
        #         print(windowSum // k)
        #         print(window)
        #         count += 1
        
        # return count

        count = 0 
        L = 0
        windowSum = 0

        for R in range(len(nums)):
            if R - L + 1 > k:
                windowSum -= nums[L]
                L += 1
            windowSum += nums[R]
            if R - L + 1 == k and (windowSum / k) >= threshold:
                print(windowSum / k)
                count += 1
        
        return count