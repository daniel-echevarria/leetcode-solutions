digits_to_letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

results = set()


class Solution:
    def letterCombinations(self, digits: str, path: str = "", index=0) -> list[str]:
        if len(path) == len(digits):
            results.add(path)
            return
        for letter in digits_to_letters[digits[index]]:
            self.letterCombinations(digits, path + letter, index + 1)


s = Solution()
s.letterCombinations("2345")
print(results)
