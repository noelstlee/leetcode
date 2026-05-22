class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = defaultdict(int) # key: letter (str) , value: occurency (int)
        tDict = defaultdict(int)

        for i in range(len(s)):
            sDict[s[i]] += 1
        
        for j in range(len(t)):
            tDict[t[j]] += 1
        
        
        for key, value in sDict.items():
            if sDict[key] != tDict[key]:
                return False
        
        return True