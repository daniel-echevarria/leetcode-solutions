class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        counts = [students.count(0), students.count(1)]

        for s in sandwiches:
            if counts[s] == 0:
                return counts[1 - s]
            counts[s] -= 1
        return sum(counts)


students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
# students = [1, 1, 1, 0, 0, 1]
# sandwiches = [1, 0, 0, 0, 1, 1]
s = Solution()
print(s.countStudents(students, sandwiches))
