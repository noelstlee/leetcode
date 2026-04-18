class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer problem
        # first filter out the blank spaces
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c.lower()

        # now use two pointers in a cleaned string without blankspaces
        p1 = 0
        p2 = len(clean) - 1
        # iterate thru clean checking elements one by one
        while p1 < p2:
            if clean[p1] != clean[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1
        return True

        