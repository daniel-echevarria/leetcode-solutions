from collections import deque
import re

# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23


class Solution:
    def calculate(self, s: str) -> int:
        clean = list("".join(s.split("+")))
        print(clean)


ex1 = "(1+(4+5+2)-3)+(6+8)"
s = Solution()
s.calculate(ex1)
# algo
# split the string
# declare a stack
# iterate through the splitted string and push the elements following this logic:
# if it's a white space, continue (ignore)
#
