class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        top = m - 1
        bot = n - 1
        write = m + n - 1

        while bot != -1:
            if top == -1 or nums1[top] < nums2[bot]:
                nums1[write] = nums2[bot]
                bot -= 1
            else:
                nums1[write] = nums1[top]
                top -= 1
            write -= 1
