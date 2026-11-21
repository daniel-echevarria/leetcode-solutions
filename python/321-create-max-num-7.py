class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def get_max(num, size):
            n = len(num)
            drop = n - size
            stack = []

            for d in num:
                while stack and drop and stack[-1] < d:
                    stack.pop()
                    drop -= 1
                stack.append(d)

            return stack[:size]

        def merge(a, b):
            i = j = 0
            merged = []

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

        for i in range(max(0, k - len(nums2)), min(len(nums1), k) + 1):
            a = get_max(nums1, i)
            b = get_max(nums2, k - i)
            res = max(res, merge(a, b))

        return res


nums1 = [6, 7]
nums2 = [6, 0, 4]
s = Solution()
print(s.maxNumber(nums1, nums2, 5))
