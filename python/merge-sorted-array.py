class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        zeroes_left = n
        total_length = m + n
        while i < total_length and j < n:
            if nums1[i] > nums2[j]:
                nums1[total_length - zeroes_left] = nums1[i]
                nums1[i] = nums2[j]
                zeroes_left -= 1
                j += 1
            else:
                i += 1
        for z in range(zeroes_left):
            idx1 = total_length - z - 1
            idx2 = n - z - 1
            nums1[idx1] = nums2[idx2]
        return nums1


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1
        j = n - 1
        z = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[z] = nums1[i]
                i -= 1
            else:
                nums1[z] = nums2[j]
                j -= 1
            z -= 1
        while j >= 0:
            nums1[z] = nums2[j]
            j -= 1
            z -= 1
        return (nums1, i, j)


# Algo
# iterate through both arrays and compare the values
# if the value of the nums2 array is smaller than the value in the nums1
# swap the current value of nums1 with a 0 and replace the current
# value with the value from nums2
# in the end for as many 0 lefts add the rest of the array
# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# nums1 = [4, 0, 0, 0, 0, 0]
# nums2 = [1, 2, 3, 5, 6]


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        return nums1


nums1 = [1, 2, 4, 5, 6, 0, 0]
nums2 = [3, 4]
m = 5
n = 2

s = Solution()
print(s.merge(nums1, m, nums2, n))
