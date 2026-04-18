class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        num_hash = defaultdict(int)
        for num in nums:
            num_hash[num] += 1

        # Sort items by frequency
        sorted_items = sorted(num_hash.items(), key=lambda x: x[1], reverse=True)
        
        # Return top k keys
        return [item[0] for item in sorted_items[:k]]