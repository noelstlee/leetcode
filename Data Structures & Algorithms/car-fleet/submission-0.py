class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [] # list of tuples of (position, speed)
        for i in zip(position, speed):
            pair.append(i)
        stack = [] # stack for fleet's front
        
        pair.sort(reverse=True) # the closest pair to the target comes first

        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)


            
        

            

        