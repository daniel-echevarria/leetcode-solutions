class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        stack = []

        for n in arr:
            while stack and stack[-1] < n:
                stack.pop()
            if stack and stack[-1] <= n:
                return False
            stack.append(n)
        return 1 < len(stack) < len(arr)


s = Solution()
# arr = [3, 4, 5, 4, 2, 1]
# arr = [1, 2, 2, 3, 2, 1]
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
arr = [1, 7, 9, 5, 4, 1, 2]
print(s.validMountainArray(arr))
