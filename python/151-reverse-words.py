class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = []
        while s:
            res.append(s.pop())
        return " ".join(res)


s = Solution()
st = "  hello world  "
print(s.reverseWords(st))

# Algo
# split the sentence at spaces
# while there are words in the list pop and trim them
# return the concatenated result
