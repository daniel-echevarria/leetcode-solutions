import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return -nums[0]


s = Solution()
# nums = [3, 2, 1, 5, 6, 4]
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(s.findKthLargest(nums, 2))
