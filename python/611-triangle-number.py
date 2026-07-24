# class Solution:
#     def triangleNumber(self, nums: list[int]) -> int:
#         n = len(nums)
#         if n < 3:
#             return 0
#         if n == 3:
#             return 1

#         nums.sort()

#         counts = 0
#         for k in range(n - 1, -1, -1):
#             i, j = 0, 1
#             while


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        counts = 0
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    counts += j - i
                    j -= 1
                else:
                    i += 1
        return counts


nums = [2, 2, 3, 4]
# nums = [4, 2, 3, 4]
# nums = [1, 2, 2, 3, 4, 7, 8]
s = Solution()
print(s.triangleNumber(nums))
