class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        days = 1
        while self.stack and self.stack[-1][0] <= price:
            _, d = self.stack.pop()
            days += d
        self.stack.append((price, days))
        return days


# Your StockSpanner object will be instantiated and called as such:
stockSpanner = StockSpanner()
print(
    stockSpanner.next(100),
    stockSpanner.next(80),
    stockSpanner.next(60),
    stockSpanner.next(70),
    stockSpanner.next(60),
    stockSpanner.next(75),
    stockSpanner.next(85),
)
