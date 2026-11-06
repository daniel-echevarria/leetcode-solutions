class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def get_max(number: list[int], size: int):
            stack = []
            drop = len(number) - size

            for num in number:
                while stack and drop and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            return stack[:size]

        def merge(a: list[int], b: list[int]):
            res = []

            i = j = 0

            while i < len(a) and j < len(b):
                if a[i:] > b[j:]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            res.extend(a[i:] + b[j:])
            return res

        res = []

        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            a = get_max(nums1, i)
            b = get_max(nums2, k - i)
            res = max(res, merge(a, b))

        return res


# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5

s = Solution()
print(s.maxNumber(nums1, nums2, k))
