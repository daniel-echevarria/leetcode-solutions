class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s + s)


s = Solution()
st = "abcde"
goal = "abced"
print(s.rotateString(st, goal))
