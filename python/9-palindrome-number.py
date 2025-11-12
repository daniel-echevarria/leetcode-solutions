class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        y = 0
        while x > 0:
            quotient, remainder = divmod(x, 10)
            x = quotient
            y = y * 10 + remainder
        return original == y
