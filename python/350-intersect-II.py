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


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
