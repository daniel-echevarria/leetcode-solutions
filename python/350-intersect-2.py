from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        counts = Counter(nums2)
        res = []
        for char in nums1:
            if counts[char]:
                res.append(char)
                counts[char] -= 1
        return res
