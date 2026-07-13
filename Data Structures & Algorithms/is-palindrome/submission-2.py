class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c.lower()

        L, R = 0, len(clean) - 1

        while L < R:
            if clean[L] != clean[R]:
                return False
            L += 1
            R -= 1
        
        return True