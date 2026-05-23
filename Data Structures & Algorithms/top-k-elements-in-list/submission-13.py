class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # key: unique element of nums, value: frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # Ex: {1: 1, 2: 2, 3: 3}
        # find the k most frequent element
        res = [] # output
        occur = [] # list of occurencies (frequencies) of each unique element of nums and then sort it
        
        for value in freq.values():
            occur.append(value)
        occur.sort(reverse=True) # sort decreasing

        for i in range(k):
            for key, value in freq.items():
                if value == occur[i]:
                    res.append(key)
                    del freq[key]
                    break
        return res
        

