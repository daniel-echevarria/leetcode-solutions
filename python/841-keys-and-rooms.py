from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        queue = deque([0])
        visited = set([0])
        while queue:
            key = queue.popleft()
            for k in rooms[key]:
                if k not in visited:
                    visited.add(k)
                    queue.append(k)
        return len(visited) == len(rooms)
