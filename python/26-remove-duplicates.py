class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        i = j = 0
        uniques = 0

        while j < n - 1:

            for k in range(j, n):
                if nums[k] == nums[j]:
                    continue
                i += 1
                nums[i] = nums[k]
                j = k
                uniques += 1
                break
        return uniques + 1


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        l = r = 0
        while r < n:
            while r < n and nums[r] == nums[l]:
                r += 1
            if r == n:
                return l + 1
            l += 1
            nums[l] = nums[r]


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r] == nums[r - 1]:
                continue
            nums[l] = nums[r]
            l += 1

        return l


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            nums[write] = nums[i]
            write += 1
        return write


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1, 1]
s = Solution()
print(s.removeDuplicates(nums))
