class Solution:
    def isPalindrome(self, s: str) -> bool:
        base = "".join([char.lower() for char in s if char.isalnum()])
        return base == base[::-1]
