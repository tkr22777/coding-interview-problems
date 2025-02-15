from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        ops = {"*", "/", "+", "-"}

        def operate(oper1: str, oper2: str, op: str) -> int:
            if op == "*":
                return int(oper1) * int(oper2)
            elif op == "/":
                return int(int(oper1) / int(oper2))
            elif op == "+":
                return int(oper1) + int(oper2)
            else:
                return int(oper1) - int(oper2)

        stk = [tokens[0]]

        i = 1
        while stk:
            if i < len(tokens):
                token = tokens[i]
                if token in ops:
                    oper1 = stk.pop()
                    oper2 = stk.pop()
                    res = operate(oper2, oper1, token)
                    # print(f"o1: {oper1} o2: {oper2}, tok: {token} ,res: {res}")
                    stk.append(str(res))
                else:
                    stk.append(token)
                i += 1
            else:
                stk.pop()
        return res


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])) 