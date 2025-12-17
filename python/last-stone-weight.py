import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            stoneY = heapq.heappop(max_heap)
            stoneX = heapq.heappop(max_heap)
            heapq.heappush(max_heap, -abs(stoneY - stoneX))
        return -max_heap[0]


stones = [2, 7, 4, 1, 8, 1]
s = Solution()
print(s.lastStoneWeight(stones))
