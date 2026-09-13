class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for string in strs:
            occurency = [0] * 26
            for i in range(len(string)):
                occurency[ord(string[i]) - ord('a')] += 1
            anagram[tuple(occurency)].append(string)
        
        res = []
        for key, value in anagram.items():
            res.append(value)
        return res