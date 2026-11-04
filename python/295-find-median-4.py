import heapq


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or num > -self.left[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        if len(self.left) < len(self.right):
            smallest = heapq.heappop(self.right)
            heapq.heappush(self.left, -smallest)
        elif len(self.left) > len(self.right) + 1:
            biggest = -heapq.heappop(self.left)
            heapq.heappush(self.right, biggest)

    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2
        return -self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
