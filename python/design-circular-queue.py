class QueueNode:
    def __init__(self, val, pos, nxt, prev):
        self.val = val
        self.pos = pos
        self.nxt = nxt
        self.prev = prev


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.front = QueueNode("root", -1, None, None)
        self.back = self.front

    def enQueue(self, value: int) -> bool:
        if self.front.val == "root" and self.back.val == "root":
            newRoot = QueueNode(value, 0, None, None)
            self.front = newRoot
            self.back = newRoot
            return True
        back = self.back
        front = self.front
        if back.pos == self.size - 1:
            if front.pos == 0:
                return False
            else:
                current = front
                while current.prev:
                    current.pos -= 1
                    current = current.prev
            print(front.pos)
        newBack = QueueNode(value, back.pos + 1, back, None)
        back.prev = newBack
        self.back = newBack
        return True

    def deQueue(self) -> bool:
        front = self.front
        if front.val == "root" and self.back.val == "root":
            return False
        if front.prev:
            front.prev.nxt == None
            self.front = front.prev
            return True
        self.front = QueueNode("root", -1, None, None)
        self.back = self.front
        return True

    def Front(self) -> int:
        if self.front.val == "root":
            return -1
        return self.front.val

    def Rear(self) -> int:
        if self.back.val == "root":
            return -1
        return self.back.val

    def isEmpty(self) -> bool:
        return self.front.val == "root" and self.back.val == "root"

    def isFull(self) -> bool:
        return self.back.pos == self.size - 1 and self.front.pos == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
