class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)

        l, r = 0, n - 1
        vowels = set("aeiou")

        while l < r:
            while l < r and s[l].lower() not in vowels:
                l += 1
            while l < r and s[r].lower() not in vowels:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)
