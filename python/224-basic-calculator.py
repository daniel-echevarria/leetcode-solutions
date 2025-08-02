from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        if s.isdigit():
            return int(s)
        filtered = filter(lambda char: char != " ", s)
        array = list(filtered)
        stack = deque()
        operators = "-+"

        def add_or_subtract(operator, a, b):
            if operator == "+":
                return f"{int(a) + int(b)}"

            if operator == "-":
                return f"{int(a) - int(b)}"

        for el in array:
            if el.isdigit() and stack and stack[-1] in operators:
                if stack[-2].isdigit():
                    operator = stack.pop()
                    left = stack.pop()
                    stack.append(add_or_subtract(operator, left, el))
            elif el == ")":
                right = stack.pop()
                _ = stack.pop()
                if not stack:
                    stack.append(right)
                elif len(stack) == 1:
                    stack.pop()
                    stack.append(add_or_subtract(right * -1))
                else:
                    operator = stack.pop()
                    left = stack.pop()
                    stack.append(add_or_subtract(operator, left, right))
            else:
                stack.append(el)
        return int(stack[0])


my_string = "(1+(4+5+2)-3)+(6+8)"
s = Solution()
s.calculate(my_string)


# Remove the white space from the string
# Split into a list
# Create a stack
# append the elements to the stack
# If the current element is a digit
# check if the previous element is a sign (-, +)
# If it is check the previous element if it's a digit
# pop the last two elements and append the result of the operation
# If the current element is a ')'
# pop the last 2 elements
# check if the previous element is a sign
# if it check if the number before is a digit
# if it is compute the result
# If there's nothing behind the sign, replace the sign with the current number * -1
