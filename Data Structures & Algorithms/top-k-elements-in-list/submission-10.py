class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = defaultdict(int)
        out = []
        for n in nums:
            numMap[n] += 1
        
        countList = []
        
        for j in numMap.values():
            countList.append(j)
        countList.sort(reverse=True)

        for i in range(k):
            for key, value in numMap.items():
                if value == countList[i]:
                    out.append(key)
                    numMap[key] = -1

        return out

                