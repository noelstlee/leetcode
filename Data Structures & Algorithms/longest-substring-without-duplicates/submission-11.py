class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupeCheck = set()
        L = 0
        res = 0

        for R in range(len(s)):
            while s[R] in dupeCheck:
                dupeCheck.remove(s[L])
                L += 1
            dupeCheck.add(s[R])
            res = max(res, R - L + 1)

        return res 

        