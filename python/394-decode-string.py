class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        sub = ""
        i = 0
        count = 0
        while i < len(s):
            if s[i].isalpha():
                res += s[i]
                i += 1
                continue
            if s[i].isnumeric():
                count = int(s[i])
                i += 2
            while s[i] != "]":
                sub += s[i]
                i += 1
            res += sub * count
            sub = ""
            i += 1
        return res


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
                continue
            sub = []
            while stack and stack[-1] != "[":
                sub.append(stack.pop())
            stack.pop()
            num = []
            while stack and stack[-1].isnumeric():
                num.append(stack.pop())
            count = int("".join(reversed(num)))
            sub_res = sub[::-1] * count
            stack.extend(sub_res)
        return "".join(stack)


# iterate until meeting a ]
# once meeting that pop from the stack until meeting the [
# push the string inside reverse as many times as the number
# keep going until the end of the string

# st = "2[abc]3[cd]ef"
# st = "3[a2[c]]"
st = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
s = Solution()
print(s.decodeString(st))

# Algo, when meeting a number
# start a count
# get the string out moving once, storing the string until the ]
# then append that many times the string to the result
# do that till  the end of the string
