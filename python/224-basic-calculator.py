class Solution:
    def calculate(self, s: str) -> int:
        def helper(it):
            total, sign, num = 0, 1, 0
            for char in it:
                if char == " ":
                    continue
                elif char.isdigit():
                    num = num * 10 + int(char)
                elif char in "-+":
                    total += num * sign
                    num = 0
                    sign = 1 if char == "+" else -1
                elif char == "(":
                    total += helper(it) * sign
                    num = 0
                elif char == ")":
                    total += num * sign
                    return total
            return total + num * sign

        result = helper(iter(s))
        return result
