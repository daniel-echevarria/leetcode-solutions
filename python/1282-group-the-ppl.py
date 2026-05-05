from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups = []
        my_dict = defaultdict(list)

        for i, s in enumerate(groupSizes):
            my_dict[s].append(i)
            if len(my_dict[s]) == s:
                groups.append(my_dict[s])
                my_dict[s] = []
        return groups


groupSizes = [3, 3, 3, 3, 3, 1, 3]
s = Solution()
print(s.groupThePeople(groupSizes))
