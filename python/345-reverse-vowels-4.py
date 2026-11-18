class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n = len(s)

        vowels = set("aeiou")
        l, r = 0, n - 1

        while l < r:
            while l < r and s[l].lower() not in vowels:
                l += 1
            while l < r and s[r].lower() not in vowels:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return "".join(s)
