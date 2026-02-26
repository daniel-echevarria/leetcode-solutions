import heapq


class MedianFinder:

    def __init__(self):
        self.center = []
        self.smaller = []
        self.bigger = []

    def total_len(self):
        return len(self.center) + len(self.smaller) + len(self.bigger)

    def data_is_even(self):
        return self.total_len() % 2 == 0

    def addNum(self, num: int) -> None:
        if len(self.center) < 2:
            self.center.append(num)
            return

        if self.total_len() == 2:
            self.center.sort()

        if self.center[0] < num < self.center[1]:
            if len(self.smaller) <= len(self.bigger):
                heapq.heappush(self.smaller, -self.center[0])
                self.center[0] = num
            else:
                heapq.heappush(self.bigger, self.center[1])
                self.center[1] = num
        elif num <= self.center[0]:
            if len(self.smaller) <= len(self.bigger):
                heapq.heappush(self.smaller, -num)
            else:
                heapq.heappush(self.smaller, -num)
                biggest_in_smaller = -heapq.heappop(self.smaller)
                heapq.heappush(self.bigger, self.center[1])
                self.center[1] = self.center[0]
                self.center[0] = biggest_in_smaller
        else:
            if len(self.smaller) <= len(self.bigger):
                heapq.heappush(self.bigger, num)
                smallest_in_bigger = heapq.heappop(self.bigger)
                heapq.heappush(self.smaller, -self.center[0])
                self.center[0] = self.center[1]
                self.center[1] = smallest_in_bigger
            else:
                heapq.heappush(self.bigger, num)

    def findMedian(self) -> float:
        if self.data_is_even():
            return sum(self.center) / 2
        else:
            return self.center[0]


# Algo:
# create a center array that will keep the two central elements of the data
# create a max heap for the smaller than center elements
# create a min heap for the bigger than center elements
# so long as the center is smaller than 2, just push the elements to it
# we will always try to keep the sizes of bigger and smaller element as close as possible
# when adding a number if it's in between the two central elements
# check the bucket with the least elements, push the correct element to it
# add the new element to the center
# if the number is not between the center, check if adding it to the correct
# bucket would improve balance. if yes just add it to the bucket
# otherwise shift the center (pushing the correct element to it's bucket)
# and adding the next element in the heap from the other side (pop)
# finally add the current element to the correct bucket heap

#

# Your MedianFinder object will be instantiated and called as such:


def main():
    obj = MedianFinder()
    obj.addNum(6)
    print(obj.findMedian())
    obj.addNum(10)
    print(obj.findMedian())
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(6)
    print(obj.findMedian())
    obj.addNum(5)
    print(obj.findMedian())
    obj.addNum(0)
    print(obj.findMedian())
    obj.addNum(6)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
    obj.addNum(1)
    print(obj.findMedian())
    obj.addNum(0)
    print(obj.findMedian())
    obj.addNum(0)
    print(obj.findMedian())
    param_2 = obj.findMedian()


main()
