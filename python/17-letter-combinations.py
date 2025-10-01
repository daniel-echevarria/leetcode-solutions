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
