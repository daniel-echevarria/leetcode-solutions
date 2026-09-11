class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)

        # Remove extra spaces in-place
        write = 0
        for char in chars:
            if char != " " or (write > 0 and chars[write - 1] != " "):
                chars[write] = char
                write += 1

        if write > 0 and chars[write - 1] == " ":
            write -= 1

        chars = chars[:write]

        # Reverse entire string
        chars.reverse()

        # Reverse each word
        start = 0
        for i in range(len(chars) + 1):
            if i == len(chars) or chars[i] == " ":
                chars[start:i] = chars[start:i][::-1]
                start = i + 1

        return "".join(chars)


st = " a good   example   "
s = Solution()
print(s.reverseWords(st))
