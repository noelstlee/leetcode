class Solution:
    def isValid(self, s: str) -> bool:
        check = {")": "(", "]": "[", "}": "{"}
        stack = [] # for ensuring order of closing brackets after opening

        if len(s) % 2 == 1: return False

        for c in s:
            if c in check: # closed brackets
                if stack and stack.pop() == check[c]:
                    continue
                else:
                    return False
            else: # open brackets
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False