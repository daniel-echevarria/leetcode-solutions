class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        total_len = m + n
        half = total_len // 2

        l, r = 0, m

        while True:
            i = (l + r) // 2
            j = half - i

            left1 = float("-inf") if i < 1 else nums1[i - 1]
            right1 = float("inf") if i >= m else nums1[i]
            left2 = float("-inf") if j < 1 else nums2[j - 1]
            right2 = float("inf") if j >= n else nums2[j]

            if left1 <= right2 and left2 <= right1:
                if total_len % 2:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2

            if left1 > right2:
                r = i - 1
            else:
                l = i + 1


s = Solution()
nums1 = [1, 2]
nums2 = [3, 4]

print(s.findMedianSortedArrays(nums1, nums2))

n = 1
count = 0
while n < 13:
 if n & 13:
