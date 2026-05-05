class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        prefix = []
        equal = []
        suffix = []
        for n in nums:
            if n < pivot:
                prefix.append(n)
            elif n > pivot:
                suffix.append(n)
            else:
                equal.append(n)
        return prefix + equal + suffix


nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10

s = Solution()
print(s.pivotArray(nums, pivot))
