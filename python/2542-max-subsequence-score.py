import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)

        total = 0
        heap = []
        max_score = 0

        for n2, n1 in pairs:
            heapq.heappush(heap, n1)
            total += n1

            if len(heap) > k:
                removed = heapq.heappop(heap)
                total -= removed
            if len(heap) == k:
                max_score = max(max_score, total * n2)
        return max_score


nums1 = [4, 2, 3, 16, 1]
nums2 = [7, 5, 10, 9, 6]
k = 1

s = Solution()
print(s.maxScore(nums1, nums2, k))
# make a minHeap out of (nums2, nums1)
# make a maxHeap of nums1

# pop from the minHeap and compute the maxScore using two from the maxHeap
# (if the index happens to be the same continue)
