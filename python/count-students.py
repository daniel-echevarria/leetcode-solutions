from collections import deque


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students = deque(students)
        sandwiches.reverse()
        refused_sandwich_count = 0

        while sandwiches:
            if students[0] == sandwiches[-1]:
                sandwiches.pop()
                students.popleft()
                refused_sandwich_count = 0
            else:
                students.append(students.popleft())
                refused_sandwich_count += 1
            if refused_sandwich_count == len(students):
                return len(students)


# students = [1, 1, 0, 0]
# sandwiches = [0, 1, 0, 1]
students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
s = Solution()
print(s.countStudents(students, sandwiches))
