class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.front_idx = 0
        self.rear_idx = 0
        self.queue = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.rear_idx < self.size:
            self.queue[self.rear_idx] = value
            self.rear_idx += 1
        else:
            self.front_idx -= 1
            self.queue[self.front_idx] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front_idx] = -1
        self.front_idx += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front_idx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        print(self.rear_idx)
        print(self.queue[self.rear_idx - 1])
        return self.queue[self.rear_idx - 1]

    def isEmpty(self) -> bool:
        return self.front_idx == self.rear_idx

    def isFull(self) -> bool:
        return self.rear_idx - self.front_idx == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
