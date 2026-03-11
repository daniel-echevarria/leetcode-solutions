class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
            if i > len(s) - 1:
                return True
        return False


s = Solution()
st = "apc"
t = "ahbgdc"

print(s.isSubsequence(st, t))
# use two pointers
# declare a pointer i that move through s every time the chars match with t
# if we go trough t before i is bigger than s, return false
# if i is bigger than s return true
