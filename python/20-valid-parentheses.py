class Solution:
    def isValid(self, s: str) -> bool:
        matches = {")": "(", "}": "{", "]": "["}
        closing_par = matches.keys()
        stack = []
        for char in s:
            if char in closing_par:
                if not stack or stack.pop() != matches[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0


s = Solution()
print()
