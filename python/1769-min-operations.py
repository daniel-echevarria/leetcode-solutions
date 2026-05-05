class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        moving_right = [0] * n
        balls = 0
        for i in range(1, n):
            if boxes[i - 1] == "1":
                balls += 1
            moving_right[i] = moving_right[i - 1] + balls

        move_left = [0] * n
        balls = 0
        res = [0] * n
        for i in range(n - 2, -1, -1):
            if boxes[i + 1] == "1":
                balls += 1
            move_left[i] = move_left[i + 1] + balls

        res = [move_left[i] + moving_right[i] for i in range(n)]
        return res


boxes = "110"
s = Solution()
print(s.minOperations(boxes))
