class Solution:
    def __init__(self):
        self.digits_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        self.results = []

    def helper(self, digits, path="", index=0):
        if len(path) == len(digits):
            path and self.results.append(path)
            return
        for letter in self.digits_to_letters[digits[index]]:
            self.helper(digits, path + letter, index + 1)

    def letterCombinations(self, digits: str) -> list[str]:
        self.helper(digits)
        return self.results


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone = {}
        phone["2"] = ["a", "b", "c"]
        phone["3"] = ["d", "e", "f"]
        phone["4"] = ["g", "h", "i"]
        phone["5"] = ["j", "k", "l"]
        phone["6"] = ["m", "n", "o"]
        phone["7"] = ["p", "q", "r", "s"]
        phone["8"] = ["t", "u", "v"]
        phone["9"] = ["w", "x", "y", "z"]

        res = []

        def helper(path=""):
            idx = len(path)
            if idx == len(digits):
                res.append(path)
                return

            for char in phone[digits[idx]]:
                helper(path + char)

        helper()

        return res


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        n = len(digits)

        res = []
        path = []

        def backtrack(i):
            if i == n:
                res.append("".join(path))
                return

            for char in phone[digits[i]]:
                path.append(char)
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res


digits = "23"
s = Solution()
print(s.letterCombinations(digits))
