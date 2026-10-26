class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s.strip())
        n = len(s)
        l = i = 0
        r = j = n - 1
        while i < j:
            while i < j and s[i] != " ":
                i += 1
            while i < j and s[j] != " ":
                j -= 1

            temp = s[j + 1 : r + 1]
            temp.append(" ")
            s[j + 1 : r + 1] = s[l:i]
            s[l:i] = temp

            l = i
            r = j
        return s


class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s.strip())
        n = len(s)
        l, r = 0, n - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        word_start = i = 0
        while i < n:
            if s[i] == " ":
                s[word_start:i] = s[word_start:i][::-1]
            while i < n and s[i] == " ":
                i += 1
                word_start = i
            i += 1
        s[word_start:] = s[word_start:][::-1]

        for i in range(n):
            if i > 0 and s[i] == " " and s[i - 1] == " ":
                s[i - 1] = ""

        return "".join(s)


st = "the sky is blue"
s = Solution()
print(s.reverseWords(st))
