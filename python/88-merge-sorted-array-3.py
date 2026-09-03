class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j = m - 1, n - 1
        write = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                write -= 1
                i -= 1
            else:
                nums1[write] = nums2[j]
                write -= 1
                j -= 1
        nums1[: j + 1] = nums2[: j + 1]
        return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

s = Solution()
print(s.merge(nums1, m, nums2, n))
