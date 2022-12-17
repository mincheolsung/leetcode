class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
                
        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                temp = eval(operand1 + token + operand2)
                stack.append(str(int(temp)))

        return int(stack[-1])
