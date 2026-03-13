class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = sum(c in vowels for c in s[:k])
        max_count = count
        for r in range(k, len(s)):
            if s[r - k] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1
            max_count = max(max_count, count)
        return max_count


s = Solution()
st = "leetcode"
k = 3
print(s.maxVowels(st, k))


# count the vowels in the first window
# move the window until out of bounds
# add and remove from count based on appearances and disappearances
