import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        current_capital = w
        projects_left = k
        max_capital = current_capital

        heap = []

        for i in range(len(profits)):
            heapq.heappush(heap, (capital[i], profits[i]))

        not_chosen_projects = []
        while projects_left:
            best_project = None
            best_deal = 0
            max_heap = []
            while heap and heap[0][0] <= current_capital:
                c, p = heapq.heappop(heap)
                if p > best_deal:
                    if best_project:
                        not_chosen_projects.append(best_project)
                    best_project = (c, p)
                    best_deal = p
                    continue
                not_chosen_projects.append((c, p))
            if not best_project:
                return max_capital
            _, pro = best_project
            current_capital += pro
            projects_left -= 1
            max_capital = max(max_capital, current_capital)
            for p in not_chosen_projects:
                heapq.heappush(heap, p)
            not_chosen_projects = []
        return max_capital


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        current_capital = w
        projects_left = k

        heap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(heap)
        max_heap = []

        while projects_left:
            while heap and heap[0][0] <= current_capital:
                c, p = heapq.heappop(heap)
                heapq.heappush(max_heap, (-p, c))
            if not max_heap:
                return current_capital
            pro, _ = heapq.heappop(max_heap)
            current_capital += -pro
            projects_left -= 1
        return current_capital


# While enough projects
# given a capital
# find all the possible projects you can start and pick the one that would
# give the maximum capital, keep going until there is no more projects left

k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]

s = Solution()
print(s.findMaximizedCapital(k, w, profits, capital))
