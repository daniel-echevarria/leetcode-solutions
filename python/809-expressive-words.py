class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        def is_stretchy(word):
            n = len(word)
            j = 0
            for i in range(n):
                if j > len(s) - 1:
                    return 0

                if word[i] == s[j]:
                    j += 1
                    continue

                if i == 0:
                    return 0

                count = 0
                char = s[j]
                while j < len(s) and s[j] == char:
                    j += 1
                    count += 1

                if count < 3:
                    return 0
            return 1

        res = 0
        for w in words:
            res += is_stretchy(w)
        return res


class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        n = len(s)

        def is_stretchy(word):
            i = j = 0
            while i < n - 1:
                char = s[i]
                count = 0
                while i < n - 1 and s[i] == char:
                    count += 1
                    i += 1
                if count > 2:
                    count = 1
                for _ in range(count):
                    if word[j] != char:
                        return 0
                    else:
                        j += 1
            return 1

        res = 0
        for w in words:
            res += is_stretchy(w)
        return res


class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        def is_stretchy(word):
            i = j = 0
            while i < len(s):
                char = s[i]
                count_s = 0
                while i < len(s) and s[i] == char:
                    i += 1
                    count_s += 1
                if j > len(word) - 1:
                    return 0
                char_w = word[j]
                count_w = 0
                if char_w != char:
                    return 0
                while j < len(word) and word[j] == char_w:
                    j += 1
                    count_w += 1
                if count_s < 3 and count_s != count_w or count_w > count_s:
                    return 0
            return i == len(s) and j == len(word)

        res = 0
        for w in words:
            res += is_stretchy(w)
        return res


# st = "heeellooo"
# words = ["hello", "hi", "helo"]
# st = "zzzzzyyyyy"
# words = ["zzyy", "zy", "zyy"]
# st = "abcd"
# words = ["abc"]
# st = "heeelllooo"
# words = ["hellllo"]
st = "abccc"
words = ["abcd"]

s = Solution()
print(s.expressiveWords(st, words))
