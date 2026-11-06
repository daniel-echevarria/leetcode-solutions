class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def get_max(number: list[int], size: int):
            stack = []
            drop = len(number) - size

            for d in number:
                while stack and drop and stack[-1] < d:
                    stack.pop()
                    drop -= 1
                stack.append(d)
            return stack[:size]

        def merge(a, b):
            merged = []
            i = j = 0

            while i < len(a) and j < len(b):
                if a[i:] >= b[j:]:
                    merged.append(a[i])
                    i += 1
                else:
                    merged.append(b[j])
                    j += 1

            merged.extend(a[i:])
            merged.extend(b[j:])
            return merged

        res = []

        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            a = get_max(nums1, i)
            b = get_max(nums2, k - i)
            res = max(res, merge(a, b))

        return res
