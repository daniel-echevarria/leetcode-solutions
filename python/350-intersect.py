class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        res = []
        l = r = 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                l += 1
            elif nums1[l] > nums2[r]:
                r += 1
            else:
                res.append(nums1[l])
                l += 1
                r += 1
        return res
