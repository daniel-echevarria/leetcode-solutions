class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0
        res = []
        for r, char in enumerate(s):
            if char == " ":
                res.append(s[l:r][::-1])
                res.append(" ")
                l = r + 1
        res.append(s[l : r + 1][::-1])
        return "".join(res)


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(map(lambda x: "".join(list(reversed(x))), s.split(" "))))


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split())


st = "Let's take LeetCode contest"
s = Solution()
print(s.reverseWords(st))
