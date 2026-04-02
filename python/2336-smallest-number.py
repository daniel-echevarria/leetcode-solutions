import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        return heapq.heappop(self.heap)

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap, num)


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.added = set()
        self.next_num = 1

    def popSmallest(self) -> int:
        if self.heap:
            val = heapq.heappop(self.heap)
            self.added.remove(val)
            return val
        val = self.next_num
        self.next_num += 1
        return val

    def addBack(self, num: int) -> None:
        if num >= self.next_num or num in self.added:
            return
        self.added.add(num)
        heapq.heappush(self.heap, num)


obj = SmallestInfiniteSet()
print(obj.popSmallest())
print(obj.popSmallest())
obj.addBack(1)
print(obj.popSmallest())
print(obj.popSmallest())
