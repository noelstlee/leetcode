class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = set()
        operator.add("+")
        operator.add("-")
        operator.add("*")
        operator.add("/")

        for token in tokens:
            if token in operator:
                if stack:
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    if token == "+":
                        stack.append(num1 + num2)
                    elif token == "-":
                        stack.append(num1 - num2)
                    elif token == "*":
                        stack.append(num1 * num2)
                    elif token == "/":
                        stack.append(int(num1 / num2))
            else:
                stack.append(token)
        
        return int(stack.pop())