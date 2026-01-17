class Solution:
    def scoreBalance(self, s: str) -> bool:
        alpha = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        prefix = []
        curr = 0
        for char in s:
            curr += alpha.index(char) + 1
            prefix.append(curr)
        total = prefix[-1]
        return True if total / 2 in prefix else False
