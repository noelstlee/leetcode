class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # initialize an array for the entire alphabet count (26 chars)
        alpha = [0] * 26
        for i in range(len(s)):
            alpha[ord(s[i]) - ord('a')] += 1
            alpha[ord(t[i]) - ord('a')] -= 1
        
        # now check if all alpha values are 0
        for val in alpha:
            if val != 0:
                return False
        return True
