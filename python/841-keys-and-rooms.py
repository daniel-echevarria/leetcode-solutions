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


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set([0])
        keys = [0]
        while keys:
            current_key = keys.pop()
            for key in rooms[current_key]:
                if key not in visited_rooms:
                    keys.append(key)
        return len(visited_rooms) == len(rooms)


# start by visiting first room
# add that room to visited rooms
# then for each key in the room, add it to a set of keys if it's not in visited and not in the set
# for each key in the set
# recurse
