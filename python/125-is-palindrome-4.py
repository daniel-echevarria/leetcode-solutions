class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [char.lower() for char in s if char.isalnum()]
        return clean == clean[::-1]


st = "A man, a plan, a canal: Panama"
s = Solution()
print(s.isPalindrome(st))
