from collections import deque
import re


class Solution:
    def calculate(self, s: str) -> int:
        # clean = list("".join(s.split("+")))
        # print(clean)
        clean = list(s)
        print(clean)
        de = deque([])
        for char in clean:
            if char == "(" or char == "-" or char == "+":
                de.append(char)
            elif char.isnumeric():
                if len(de) == 0 or de[-1] == "(":
                    de.append(int(char))
                elif de[-1] == "-":
                    de.pop()
                    de.append(int(char) * -1)
                elif de[-1] == "+":
                    de.pop()
                    prev = de.pop()
                    de.append(int(char) + prev)
                else:
                    prev = de.pop()
                    de.append(f"{prev}{char}")
            elif char == ")":
                c = char
                res = 0
                while True:
                    c = de.pop()
                    if c == "(":
                        if len(de) == 0 or not de[-1] == "-":
                            de.append(res)
                            break
                        de.pop()
                        de.append(res * -1)
                        break
                    res += int(c)
        print(de)
        without_plus = filter(lambda x: x != "+", de)
        final = map(lambda x: int(x), without_plus)
        result = sum(final)
        print(result)
        return result


ex1 = "(1-(4+5+2)-3)+(6+8)"
ex2 = "1 + 1"
ex3 = " 2-1 + 2 "
ex4 = "2147483647"

s = Solution()
s.calculate(ex1)
s.calculate(ex2)
s.calculate(ex3)
s.calculate(ex4)
# algo
# split the string
# declare a stack
# iterate through the splitted string and push the elements following this logic:
# if it's a white space, continue (ignore)
#
