class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def get_max(num, size):
            if not size:
                return []

            stack = []
            drop = len(num) - size

            if not drop:
                return num[:size]

            for n in num:
                while stack and drop and stack[-1] < n:
                    stack.pop()
                    drop -= 1
                stack.append(n)

            return stack[:size]

        def merge(a, b):
            merged = []
            i = j = 0

            while i < len(a) and j < len(b):
                if a[i:] > b[j:]:
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


nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5

s = Solution()
print(s.maxNumber(nums1, nums2, k))
