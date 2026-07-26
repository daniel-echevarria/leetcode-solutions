class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r, deletions):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if deletions == 0:
                        return False
                    return isPalindrome(l + 1, r, 0) or isPalindrome(l, r - 1, 0)
            return True

        return isPalindrome(0, len(s) - 1, 1)


st = "abc"
s = Solution()
print(s.validPalindrome(st))
