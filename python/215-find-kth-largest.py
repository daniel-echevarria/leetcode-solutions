import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        for _ in range(k):
            biggest = heapq.heappop(max_heap)
        return -biggest


s = Solution()
# nums = [3, 2, 1, 5, 6, 4]
# k = 2
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(s.findKthLargest(nums, k))
