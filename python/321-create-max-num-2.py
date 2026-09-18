class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def max_sub(nums, length):
            sub = []
            remove = len(nums) - length

            for num in nums:
                while sub and sub[-1] < num and remove > 0:
                    sub.pop()
                    remove -= 1
                sub.append(num)
            return sub[:length]

        def merge(a, b):
            merge = []

            while a and b:
                if a > b:
                    merge.append(a.pop(0))
                else:
                    merge.append(b.pop(0))
            merge.extend(a)
            merge.extend(b)
            return merge

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        best = []
        for k1 in range(start, end + 1):
            k2 = k - k1

            sub1 = max_sub(nums1, k1)
            sub2 = max_sub(nums2, k2)
            candidate = merge(sub1, sub2)
            best = max(candidate, best)
        return best


nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5

s = Solution()
print()
