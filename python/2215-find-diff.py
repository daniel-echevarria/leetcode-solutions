class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]


# Iterate over nums1 while creating a dict

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

s = Solution()
print(s.findDifference(nums1, nums2))
