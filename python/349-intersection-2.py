class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        inter = [el for el in nums1 if el in nums2]
        return list(set(inter))


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        return [el for el in nums1 if el in nums2]


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))
