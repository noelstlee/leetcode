class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupCheck = set()
        L = 0
        if not s:
            return 0
            
        dupCheck.add(s[L])
        maxLength = 1

        for R in range(1, len(s)):
            if s[R] not in dupCheck:
                dupCheck.add(s[R])
            else:
                maxLength = max(maxLength, len(dupCheck))
                while s[R] in dupCheck:
                    dupCheck.discard(s[L])
                    L += 1
                dupCheck.add(s[R])
        
        return max(maxLength, len(dupCheck))
