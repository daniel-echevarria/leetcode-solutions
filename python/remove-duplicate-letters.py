from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        seen = set()

        for c in s:
            while stack and stack[-1] > c and count[stack[-1]] > 0 and c not in seen:
                seen.remove(stack[-1])
                stack.pop()
            if c not in seen:
                stack.append(c)
                seen.add(c)
            count[c] -= 1
        return "".join(stack)


s = Solution()
# st = "bcabc"
# st = "cdadabcc"
# st = "ecbacba"
st = "abacb"

print(s.removeDuplicateLetters(st))

# Algo:
# Declare an array res of length s with initial empty arrays
# Iterate through the letters
# for each letter iterate through the result and push the letter to it
# if the letter is not yet present
# return the smallest res
