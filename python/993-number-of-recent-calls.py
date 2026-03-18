from collections import deque


class RecentCounter:

    def __init__(self):
        self.window = deque()

    def ping(self, t: int) -> int:
        self.window.append(t)
        while self.window and self.window[0] < t - 3000:
            self.window.popleft()
        return len(self.window)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# create a window
# every time a ping is made, deque all values that are smaller than ping time - 3000
# push the length of the window to the result
