class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def get_max(num, size):
            stack = []
            drop = len(num) - size

            for d in num:
                while stack and drop and stack[-1] < d:
                    stack.pop()
                    drop -= 1
                stack.append(d)

            return stack[:size]

        def merge(a, b):
            combined = []
            i = j = 0

            while i < len(a) and j < len(b):
                if a[i:] >= b[j:]:
                    combined.append(a[i])
                    i += 1
                else:
                    combined.append(b[j])
                    j += 1

            combined.extend(a[i:])
            combined.extend(b[j:])

            return combined

        res = []

        for i in range(max(0, k - len(nums2)), min(len(nums1), k) + 1):
            a = get_max(nums1, i)
            b = get_max(nums2, k - i)
            res = max(merge(a, b), res)

        return res[:k]


nums1 = [6, 6, 8]
nums2 = [5, 0, 9]
k = 3

s = Solution()
print(s.maxNumber(nums1, nums2, k))
