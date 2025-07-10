class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        available_keys = [0]
        visited_rooms_count = 0
        used_keys = set()
        while True:
            fresh_keys = []
            for key in available_keys:
                for k in rooms[key]:
                     if k not in used_keys and k not in available_keys:
                         fresh_keys.append(k)
                used_keys.add(key)
                visited_rooms_count += 1
            available_keys = fresh_keys
            if visited_rooms_count >= len(rooms):
                return True
            if len(available_keys) == 0:
                return False



