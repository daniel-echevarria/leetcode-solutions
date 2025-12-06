from collections import defaultdict


class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        times = defaultdict(int)
        stack = []
        prev_depth = 0
        prev_time = 0
        depth = 0

        for l in logs:
            fn, action, ts = l.split(":")
            fn = int(fn)
            ts = int(ts)
            if (
                action == "end"
                and stack
                and stack[-1][1] == "start"
                and stack[-1][0] == fn
            ):
                _, _, pts = stack.pop()
                total_time = ts - pts + 1
                if depth > prev_depth:
                    times[fn] += total_time - prev_time
                    prev_time = total_time
                else:
                    prev_time += total_time
            else:
                stack.append((fn, action, ts))
                depth += 1
                prev_depth += 1

        return [times[i] for i in range(n)]


# logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
n = 2

s = Solution()
print(s.exclusiveTime(n, logs))

# Algo
# Declare  an empty map times
# Declare an empty stack
# Iterate through the logs
# If the current log is an end, and the previous log is the start of
# that function, pop the start and add the time difference
# to the times map with the key of the function
# otherwise just push a workable version (tuple) of
# the log to the stack
# In the end iterate in the range n providing the sum from
# times
