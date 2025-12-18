import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        heap = []
        res = []

        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while len(res) < k:
            _, i1, i2 = heapq.heappop(heap)
            res.append([nums1[i1], nums2[i2]])

            if i2 + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))

        return res


s = Solution()
nums1 = [1, 2, 4, 5, 6]
nums2 = [3, 5, 7, 9]
k = 7
print(s.kSmallestPairs(nums1, nums2, k))


# Algo
# while the current value + the value of the other array
# is smaller or equal to the first value of the other
