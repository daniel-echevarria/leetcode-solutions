class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if not nums2:
            return nums1

        for i in range(m):
            if nums1[i] > nums2[0]:
                nums1[i], nums2[0] = nums2[0], nums1[i]
        nums1[m:] = sorted(nums2)
        print(nums1)


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        write = m + n - 1
        i, j = m - 1, n - 1

        while j >= 0:
            if i == -1 or nums2[j] > nums1[i]:
                nums1[write] = nums2[j]
                j -= 1
                write -= 1
            else:
                nums1[write] = nums1[i]
                i -= 1
                write -= 1


# nums1 = [2, 0]
# m = 1
# nums2 = [1]
# n = 1

nums1 = [0]
m = 0
nums2 = [1]
n = 1
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

s = Solution()
print(s.merge(nums1, m, nums2, n))
