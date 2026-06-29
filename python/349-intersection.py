class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first = set(nums1)
        sec = set(nums2)
        return list(first.intersection(sec))
