import heapq
import random


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return -nums[0]


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = k - 1

        def partition(left, right):
            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[right], nums[i] = nums[i], nums[right]
            if i == k:
                return nums[i]
            if i < k:
                return partition(i + 1, right)
            if i > k:
                return partition(left, i - 1)

        return partition(0, len(nums) - 1)


s = Solution()
nums = [3, 2, 1, 5, 6, 4]
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(s.findKthLargest(nums, 2))
