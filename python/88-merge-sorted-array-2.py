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
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1
        nums1[: j + 1] = nums2[: j + 1]
        return nums1


nums1 = [2, 3, 5, 0, 0, 0]
m = 3
nums2 = [-10, -5, -2]
n = 3

s = Solution()
print(s.merge(nums1, m, nums2, n))

Output: [1, 2, 2, 3, 5, 6]
