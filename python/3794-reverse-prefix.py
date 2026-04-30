class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        prefix = []
        for i in range(k):
            prefix.append(s[i])
        reversed_pre = "".join(list(reversed(prefix)))
        return reversed_pre + s[k:]


class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]


class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        left, right = 0, k - 1
        s = list(s)
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)


s = "abcd"
k = 2
so = Solution()
print(so.reversePrefix(s, k))
