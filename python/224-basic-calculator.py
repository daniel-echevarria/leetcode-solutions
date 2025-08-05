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

        for i in range(1, len(array)):
            if array[i].isdigit() and array[i - 1].isdigit():
                array[i - 1] += array[i]
                array[i] = "#"

        for el in array:
            if el == "#":
                continue
            if el.isdigit() and stack and stack[-1].lstrip("-").isdigit():
                first_digit = stack.pop()
                stack.append(first_digit + el)
            elif el.isdigit() and stack and stack[-1] in operators:
                if len(stack) == 1:
                    _ = stack.pop()
                    stack.append(f"{int(el) * -1}")
                elif len(stack) > 1 and not stack[-2].lstrip("-").isdigit():
                    _ = stack.pop()
                    stack.append(f"{int(el) * -1}")
                else:
                    operator = stack.pop()
                    left = stack.pop()
                    stack.append(add_or_subtract(operator, left, el))

            elif el == ")":
                print(stack)
                right = stack.pop()
                stack.pop()
                if not stack:
                    stack.append(right)
                elif len(stack) == 1:
                    stack.append(f"{int(right) * -1}")
                elif len(stack) == 2:
                elif stack[-1] == "(":

                    continue
                else:
                    operator = stack.pop()
                    left = stack.pop()
                    stack.append(add_or_subtract(operator, left, right))

            else:
                stack.append(el)
        res = int(stack[0])
        print(res)
        return res


my_string = "(1+(4+5+2)-3)+(6+8)"
my_string_2 = "  30"
my_string_3 = "1-(     -2)"
four = "-2+ 1"
fuck = "- (3 + (4 + 5))"
peak = "1-11"
damn = "1 + ((1 + 1) + 1)"

s = Solution()
s.calculate(my_string)
s.calculate(my_string_2)
s.calculate(my_string_3)
s.calculate(four)
s.calculate(fuck)
s.calculate(peak)
s.calculate(damn)


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
