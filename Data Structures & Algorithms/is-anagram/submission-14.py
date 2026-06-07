class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = defaultdict(int)

        # fill in the sDict with letter: count
        for sLetter in s:
            sDict[sLetter] += 1

        # check with sLetter and see if all remaining values in sDict are 0
        for tLetter in t:
            if tLetter in sDict:
                sDict[tLetter] -= 1
            else:
                return False
        
        for value in sDict.values():
            if value != 0:
                return False
        return True