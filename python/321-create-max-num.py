class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        merge = ""
        nums1_str = "".join(str(el) for el in nums1)
        nums2_str = "".join(str(el) for el in nums2)

        while nums1_str and nums2_str:
            if int(nums1_str) > int(nums2_str):
                merge += nums1_str[0]
                nums1_str = nums1_str[1:]
            else:
                merge += nums2_str[0]
                nums2_str = nums2_str[1:]
        merge += nums1_str + nums2_str

        monostack = []
        merge = [int(char) for char in merge]

        for i in range(len(merge)):
            while (
                monostack
                and monostack[-1] < merge[i]
                and (len(monostack) + len(merge) - i - 1) >= k
            ):
                monostack.pop()
            monostack.append(merge[i])
        return monostack


# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
s = Solution()
print(s.maxNumber(nums1, nums2, k))
