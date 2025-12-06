class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        print(int(-10 / 3))
        stack = []
        for t in tokens:
            if t in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[t](a, b))
            else:
                stack.append(int(t))
        return stack[-1]


s = Solution()
# tokens = ["2", "1", "+", "3", "*"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(s.evalRPN(tokens))


# Algo:
# Iterate through the tokens
# when meeting an operator
# pop the last two items operate them with the operator
# push the result and keep going
# after iteration return stack[0]
