class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana = defaultdict(int)
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            ana[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in ana:
                return False
            if ana[t[j]] == 0:
                return False
            else:
                ana[t[j]] -= 1
        return True