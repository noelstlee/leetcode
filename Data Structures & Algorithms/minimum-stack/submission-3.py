class MinStack:

    def __init__(self):
        self.stack = [] # instance attribute that is hardcoded for initialization of a list

    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        minimum = self.stack[0]
        for i in self.stack:
            minimum = min(i, minimum)
        return minimum
