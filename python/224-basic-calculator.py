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

        joined_numbers_array = [array[0]]
        for i in range(1, len(array)):
            if array[i].isdigit() and joined_numbers_array[-1].isdigit():
                joined_numbers_array[-1] += array[i]
            else:
                joined_numbers_array.append(array[i])

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
                right = stack.pop()
                left_par = stack.pop()
                if not stack or stack[-1] == "(":
                    stack.append(right)
                elif len(stack) == 1:
                    stack.pop()
                    stack.append(f"{int(right) * -1}")
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
ultime = "(9568+(9040-(380+(2042-(7115)+(6294)-(4395-(5183+9744+(7746-(1099+2718))-(9370-(8561+(9302)-(7632+(8451-(1759+(7760))-(3377+5363+9093+(8332-(4492-(1151+(1165-8833+(775+(3749)+9399))+9112+(6273+(7285-(6112-(668-(7756-4316-(582+1835-(6644+690+1204-(7197+(7897))+(7009-(7262))-7782-(7858+(7644+(9461+(2224)-(7531-1095-(891+1022)+2197-(9855)))+(6663-(7417-(6158-(3610))+(1481))-(4182+(4761)))+(5017))+(9990)+(6218)))-(2904)+(5631)-(8888)+3401+(3569))+(1135))-(3695-(7713+(3479)-(9813+(8171+(8616-8026+(4634-(6973))-(9761-(623-4782)+(2514)+(6233)))))+(6140))-(6641)-8611+(8389)+8074-(4412))-(3703)+(9688+(9513))))-(4987)))+(9647)))))))))-(2299))-(4785))))))"

s = Solution()
# s.calculate(my_string)
# s.calculate(my_string_2)
# s.calculate(my_string_3)
# s.calculate(four)
# s.calculate(fuck)
# s.calculate(peak)
# s.calculate(damn)
s.calculate(ultime)


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
