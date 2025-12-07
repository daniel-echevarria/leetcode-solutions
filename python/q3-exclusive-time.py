from collections import defaultdict


class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        times = [0] * n
        stack = []

        for l in logs:
            fn, a, ts = l.split(":")
            fn = int(fn)
            ts = int(ts)
            if a == "end" and stack[-1][1] == "start" and stack[-1][0] == fn:
                prev = stack.pop()
                total_time = ts - prev[2] + 1
                specific_time = total_time - prev[3]
                times[fn] += specific_time
                if stack:
                    stack[-1][3] += total_time
            else:
                stack.append([fn, a, ts, 0])

        return times


# Algo
# iterate through the logs
# if the current log closes the previous
# pop the previous and add the difference to the map - the inner_time_value
# and update the inner_time value
# Keep on going until all the logs where seen


# logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:7", "1:end:7", "0:end:8"]
logs = ["0:start:0", "0:start:1", "0:start:2", "0:end:3", "0:end:4", "0:end:5"]
n = 2
s = Solution()
print(s.exclusiveTime(n, logs))
