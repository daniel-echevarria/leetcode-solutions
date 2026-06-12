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


# nums = [1, 3, 2, 5, 8, 6, 4]
nums = [1, 3, 2]
s = Solution()
print(s.nextPermutation(nums))
print(nums)
