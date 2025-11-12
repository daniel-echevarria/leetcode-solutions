class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        r = len(digits) - 1
        carry = 1
        while carry:
            if r < 0:
                return [1] + digits
            digits[r] += 1
            if digits[r] < 10:
                return digits
            digits[r] = 0
            r -= 1


s = Solution()
digits = [9]
print(s.plusOne(digits))
