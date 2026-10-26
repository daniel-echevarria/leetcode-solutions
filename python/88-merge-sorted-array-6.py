class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j = m - 1, n - 1
        write = m + n - 1

        while j != -1:
            if i == -1 or nums1[i] < nums2[j]:
                nums1[write] = nums2[j]
                j -= 1
            else:
                nums1[write] = nums1[i]
                i -= 1
            write -= 1
