class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)
        idx_is_vowel = [False] * n
        vowels_in_s = []
        vowels = ["a", "e", "i", "o", "u"]
        for i in range(n):
            if s[i].lower() in vowels:
                idx_is_vowel[i] = True
                vowels_in_s.append(s[i])
        for i in range(n):
            if idx_is_vowel[i]:
                s[i] = vowels_in_s.pop()
        return "".join(s)


class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s = list(s)
        vowels = set("aeiouAEIOU")
        while l < r:
            if s[l].lower() not in vowels:
                l += 1
                continue
            if s[r].lower() not in vowels:
                r -= 1
                continue
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)


s = Solution()
# st = "IceCreAm"
st = "leetcode"
print(s.reverseVowels(st))

# Algo
# create an array the same length as s with  all values equal to false
# Iterate once through the array and each time you meet a vowel
# change the corresponding index to true and push the vowel to a vowels array
# iterate once more and each time the corresponding value is true
# pop a vowel from the vowels array
