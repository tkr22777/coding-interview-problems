from typing import List

# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)  # Using int division for negative numbers
        }
        
        for token in tokens:
            if token in ops:
                b = stack.pop()  # Second operand
                a = stack.pop()  # First operand
                stack.append(ops[token](int(a), int(b)))
            else:
                stack.append(token)
                
        return int(stack[0])


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]) == 9)
print(s.evalRPN(["4", "13", "5", "/", "+"]) == 6)
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22) 