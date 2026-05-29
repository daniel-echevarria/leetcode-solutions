from collections import deque
from collections import defaultdict


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = defaultdict(int)
        sequence = []
        for t in tasks:
            counts[t] += 1
        sorted_counts = sorted(
            [(val, key) for key, val in counts.items()], reverse=True
        )
        queue = deque(sorted_counts)
        while queue:
            distance = n + 1
            for _ in range(len(queue)):
                counts, task = queue.popleft()
                sequence.append(task)
                counts -= 1
                distance -= 1
                if counts > 0:
                    queue.append((counts, task))
            if queue:
                for _ in range(distance):
                    sequence.append("iddle")
        print(sequence)
        return len(sequence)


import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = defaultdict(int)
        for t in tasks:
            counts[t] += 1
        heap = []
        for key, val in counts.items():
            heapq.heappush(heap, (-val, key))

        res = []

        while heap:
            turn = []
            distance = n
            for _ in range(distance + 1):
                if heap:
                    count, task = heapq.heappop(heap)
                    count += 1
                    if count:
                        turn.append((count, task))
                    res.append(task)
                else:
                    if not turn:
                        continue
                    res.append("idle")
            for t in turn:
                heapq.heappush(heap, t)
        return len(res)

        # Algo
        # create a counts dict
        # out of that counts dict build a maxHeap based on the counts
        # we will iterate through a different task so long as we don't have the distance
        # we need, we will add iddles until then if needed
        # then we will use the task with the biggest count in order
        # (the key idea is that we want to start the tasks with more counts asap)


# tasks = ["A", "A", "A", "B", "B", "B"]
# n = 2

# tasks = ["A", "C", "A", "B", "D", "B"]
# n = 1

tasks = ["B", "C", "D", "A", "A", "A", "A", "G"]
n = 1


s = Solution()
print(s.leastInterval(tasks, n))


# Algo, create a dict of the counts per task
# create a queue of the tasks
# iterate the task queue while decrementing n,
# if after the iteration n is bigger than 0
# add that many 'iddles'
# if the task reaches 0 counts do not append it to the queue, otherwise do
# when there is no mor queue check the length
