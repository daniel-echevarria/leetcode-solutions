class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = n - 2
        i = r = n - 1
        while l >= 0:
            if nums[l] < nums[i]:
                r = n - 1
                while nums[r] < nums[l]:
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]
                nums[i + 1 :] = nums[i + 1 :][::-1]
                return
            l -= 1
            i -= 1
        nums.reverse()


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        l = n - 2
        i = r = n - 1

        while l >= 0:
            if nums[l] < nums[i]:
                r = n - 1

                while nums[r] <= nums[l]:
                    r -= 1

                nums[l], nums[r] = nums[r], nums[l]
                nums[i + 1 :] = nums[i + 1 :][::-1]
                return

            l -= 1
            i -= 1

        nums.reverse()


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        switch_point: int = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                switch_point = i
                break

        if switch_point == -1:
            nums.sort()
            return

        for i in range(n - 1, -1, -1):
            if nums[i] > nums[switch_point]:
                nums[i], nums[switch_point] = nums[switch_point], nums[i]
                break

        nums[switch_point + 1 :] = reversed(nums[switch_point + 1 :])
        return nums


# Algo, find the first decreasing item from the end and mark it's index, if no such item is found, just sort the array
# then iterate gain from the end and find the first element which is bigger than the
# switch point element, switch them
# then order the rest of the array

# nums = [1, 3, 2, 5, 8, 6, 4]
nums = [1, 3, 2]
s = Solution()
print(s.nextPermutation(nums))
