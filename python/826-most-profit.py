class Solution:
    def maxProfitAssignment(
        self, difficulty: list[int], profit: list[int], worker: list[int]
    ) -> int:
        dif_pro = sorted([(d, p) for d, p in zip(difficulty, profit)], reverse=True)
        worker.sort(reverse=True)
        stack = []
        for d, p in dif_pro:
            if stack and p >= stack[-1][1]:
                stack = [(d, p)]
            else:
                stack.append((d, p))
        stack.reverse()

        total = 0
        for w in worker:
            while stack and stack[-1][0] > w:
                stack.pop()
            while len(stack) > 1 and stack[-1][1] <= stack[-2][1]:
                stack.pop()
            if not stack:
                return total
            total += stack[-1][1]
        return total


class Solution:
    def maxProfitAssignment(
        self, difficulty: list[int], profit: list[int], worker: list[int]
    ) -> int:
        jobs = sorted(zip(difficulty, profit))
        workers = sorted(worker)

        best = 0
        total = 0
        i = 0

        for w in workers:
            while i < len(jobs) and jobs[i][0] <= w:
                best = max(best, jobs[i][1])
                i += 1
            total += best
        return total


# difficulty = [2, 4, 6, 8, 10]
# profit = [10, 20, 30, 40, 50]
# worker = [4, 5, 6, 7]
# difficulty = [85, 47, 57]
# profit = [24, 66, 99]
# worker = [40, 25, 25]
difficulty = [68, 35, 52, 47, 86]
profit = [67, 17, 1, 81, 3]
worker = [92, 10, 85, 84, 82]
# difficulty = [5, 50, 92, 21, 24, 70, 17, 63, 30, 53]
# profit = [68, 100, 3, 99, 56, 43, 26, 93, 55, 25]
# worker = [96, 3, 55, 30, 11, 58, 68, 36, 26, 1]


s = Solution()
print(s.maxProfitAssignment(difficulty, profit, worker))
