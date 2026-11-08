from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        counts = Counter(nums1)

        res = []

        for val in nums2:
            if counts.get(val, 0) == 0:
                continue

            res.append(val)
            counts[val] -= 1

        return res
