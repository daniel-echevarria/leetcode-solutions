import heapq


class MedianFinder:

    def __init__(self):
        self.left = []  # max_heap
        self.right = []  # min_heap

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        elif len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            max_left = -self.left[0]
            min_right = self.right[0]
            return (max_left + min_right) / 2
        else:
            return -self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
