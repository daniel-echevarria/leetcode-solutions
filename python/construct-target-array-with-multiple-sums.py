import heapq


class Solution:
    def isPossible(self, target: list[int]) -> bool:
        heap = [-n for n in target]
        heapq.heapify(heap)

        total = sum(target)

        while True:
            biggest = -heapq.heappop(heap)
            rest = total - biggest

            if biggest == 1 or rest == 1:
                return True

            if biggest <= rest or rest == 0:
                return False

            prev = biggest % rest
            if prev == 0:
                return False
            heapq.heappush(heap, -prev)
            total = rest + prev


s = Solution()
# target = [9, 3, 5]
target = [1, 1000000000]
# target = [1, 1, 1, 2]
# target = [8, 5]
# target = [1, 1, 2]

print(s.isPossible(target))
# Algo
# Notes:
# If the sum is bigger than then smallest number in the target we ca return false

# First approach:
# We create a heap that will store the possible numbers we can replace
# from the array (set turned heap)
# we iterate on that heap replacing the first char we find
# with the sum recursively.
# if at any point the sum is bigger than the smallest number we return false
# if at some point the array is like the target we change isPossible

# Second:
# Heapify the target to get the biggest value
# pop it, compute what it replaced and append back to the heap
# if at some point it's less than 1 return False
# if at some point it equals the start return true
