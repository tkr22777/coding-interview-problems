from typing import List

# Problem: Evaluate Reverse Polish Notation
# Evaluate arithmetic expressions in RPN format (postfix notation)
# where operands come before operators.
# Example: ["2", "1", "+", "3", "*"] = (2 + 1) * 3 = 9

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)  # Integer division as per problem requirement
        }
        
        for token in tokens:
            if token in ops:
                b, a = stack.pop(), stack.pop()  # Second and first operands
                stack.append(ops[token](int(a), int(b)))
            else:
                # Convert to int immediately when pushing to stack
                stack.append(int(token))
                
        return stack[0]  # No need for int() conversion here


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]) == 9)
print(s.evalRPN(["4", "13", "5", "/", "+"]) == 6)
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22) 