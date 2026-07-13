class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list) # {[char count array for each string] : list of index in strings}
        res = []

        for i in range(len(strs)):
            freq = [0] * 26
            for j in range(len(strs[i])):
                freq[ord(strs[i][j]) - ord('a')] += 1
            anaMap[tuple(freq)].append(i)
        
        for values in anaMap.values():
            appendList = []
            for index in values:
                appendList.append(strs[index])
            res.append(appendList)

        return res
        

