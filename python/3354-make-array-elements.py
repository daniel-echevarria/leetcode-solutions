class Solution:
    def try_to_solve(self, arr, curr, dir):
        while 0 <= curr <= len(arr) - 1:
            if arr[curr] == 0:
                curr += dir
                continue
            if arr[curr] > 0:
                arr[curr] -= 1
                dir = -dir
                curr += dir
        if all([x == 0 for x in arr]):
            return 1
        return 0

    def countValidSelections(self, nums: list[int]) -> int:
        valid_options = 0
        for i, n in enumerate(nums):
            if n == 0:
                valid_options += self.try_to_solve(nums.copy(), i, 1)
                valid_options += self.try_to_solve(nums.copy(), i, -1)
        return valid_options


nums = [1, 0, 2, 0, 3]
s = Solution()
print(s.countValidSelections(nums))
