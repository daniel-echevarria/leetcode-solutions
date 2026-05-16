class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        travel.append(0)
        collection_m = 0
        collection_p = 0
        collection_g = 0
        travel_time_m = 0
        travel_time_p = 0
        travel_time_g = 0

        for i, h in enumerate(garbage):
            local_m = h.count("M")
            local_p = h.count("P")
            local_g = h.count("G")
            if local_m:
                collection_m += local_m + travel_time_m
                travel_time_m = travel[i]
            else:
                travel_time_m += travel[i]
            if local_p:
                collection_p += local_p + travel_time_p
                travel_time_p = travel[i]
            else:
                travel_time_p += travel[i]
            if local_g:
                collection_g += local_g + travel_time_g
                travel_time_g = travel[i]
            else:
                travel_time_g += travel[i]

        return sum([collection_m, collection_p, collection_g])


garbage = ["G", "P", "GP", "GG"]
travel = [2, 4, 3]

s = Solution()
print(s.garbageCollection(garbage, travel))

# Algo
# iterate through the garbage array
# at each house count the garbage of each type
# for each type if the garbage is bigger than 0, add the count to the sofar trip time
# to the total time for that garbage type
# at the end of the houses sum all collection time
