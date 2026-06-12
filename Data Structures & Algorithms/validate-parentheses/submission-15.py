class Solution:
    def isValid(self, s: str) -> bool:
        closed = {")": "(", "}": "{", "]": "["}
        stack = []

        if len(s) % 2 == 1:
            return False

        for b in s:
            if b in closed:
                if stack and stack.pop() == closed[b]:
                    continue
                else:
                    return False
            else:
                stack.append(b)
        
        if not stack:
            return True
        else:
            return False
        