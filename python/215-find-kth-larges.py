import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        count = 0
        last_biggest = float("inf")
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        while count < k:
            biggest = heapq.heappop(max_heap)
            if biggest < last_biggest:
                count += 1
                last_biggest = biggest
        return last_biggest


s = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(s.findKthLargest(nums, k))
