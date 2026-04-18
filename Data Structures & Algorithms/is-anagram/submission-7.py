class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check length of both strings
        if len(s) != len(t):
            return False
        # check count of each distinct letters using hash map for (letter, count)
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
            # if there are duplicate keys (letters) while counting we add to the count
        return countS == countT