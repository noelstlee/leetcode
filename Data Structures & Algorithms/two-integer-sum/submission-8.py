class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hash map
        num_hash = {}  # value -> index
        for index, num in enumerate(nums):
            diff = target - num
            if diff in num_hash:
                return [num_hash[diff], index]
            num_hash[num] = index 
            # Track elements you’ve already seen, so that in future iterations,
            # you can quickly check if the complement (target - num) exists.
        return None