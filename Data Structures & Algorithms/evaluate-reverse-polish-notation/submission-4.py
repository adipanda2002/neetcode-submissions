class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ('+', '-', '*', '/')

        def operate(operator: str, num1: int, num2: int) -> int:
            match operator:
                case '+':
                    return num1 + num2
                case '-':
                    return num1 - num2
                case '*':
                    return num1 * num2
                case '/':
                    return int(num1 / num2)

        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                val = operate(token, num1, num2)
                stack.append(val)
            else:
                stack.append(int(token))

        return stack[-1]
    
        