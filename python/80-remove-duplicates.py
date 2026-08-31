class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)

        write = 1
        count = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                if count < 2:
                    write += 1
                    count += 1
                    continue
                else:
                    continue
            else:
                count = 1
                nums[write] = nums[i]
                write += 1
        print(nums)
        return write


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)

        write = 1
        count = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                if count < 2:
                    count += 1
                elif count == 2:
                    count += 1
                    write = i
            else:
                if count > 2:
                    nums[write] = nums[i]
                    count = 2
                else:
                    count = 1


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)

        write = 2

        for i in range(2, n):
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1
        return write


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1
        return write


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        write = read = 2
        while read < n:
            while write < n - 1 and nums[write] != nums[write - 2]:
                write += 1
            while read < n - 1 and nums[read] <= nums[write]:
                read += 1
            nums[write] = nums[read]
            write += 1
            read += 1
        return write


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1
        return write


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1
        return write


# nums = [1, 1, 1, 2, 2, 3]
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]


s = Solution()
print(s.removeDuplicates(nums))
