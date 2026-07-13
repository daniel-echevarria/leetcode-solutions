class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        dictionary.sort(key=lambda s: (-len(s), s))

        def is_sub(a, b):
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)

        for w in dictionary:
            if is_sub(w, s):
                return w

        return ""


s = "apbcplea"
dictionary = ["ale", "apple", "monkey", "plea"]

so = Solution()
print(so.findLongestWord(s, dictionary))
