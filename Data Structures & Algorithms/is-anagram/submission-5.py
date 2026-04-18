class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            for letter in s:
                if letter in t:
                    t = t.replace(letter,'',1)
                else:
                    return False
        else:
            for letter in t:
                if letter in s:
                    s = s.replace(letter,'',1)
                else:
                    return False

        return True