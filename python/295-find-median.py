class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        self.array.sort()
        curr_len = len(self.array)
        mid = curr_len // 2
        if curr_len % 2 == 0:
            return (self.array[mid] + self.array[mid - 1]) / 2
        return self.array[mid]


class MedianFinder:

    def __init__(self):
        self.lower_mid = None
        self.upper_mid = None
        self.count = 0

    def addNum(self, num: int) -> None:
        if not self.lower_mid:
            self.lower_mid = num
            self.upper_mid = num
        elif not self.upper_mid:
            if num > self.upper_mid:
                self.upper_mid = num
            else:
                self.upper_mid = self.lower_mid
                self.lower_mid = num
        else:


        self.array.append(num)

    def findMedian(self) -> float:
        self.array.sort()
        curr_len = len(self.array)
        mid = curr_len // 2
        if curr_len % 2 == 0:
            return (self.array[mid] + self.array[mid - 1]) / 2
        return self.array[mid]

class MedianFinder:

# Algo
#

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Algo
# when addnum push values to an array
# when findmedian, sort the array
# if even number given the average of the 2 central items
# otherwise give the central item
