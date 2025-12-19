import heapq


class Solution:
    def isPossible(self, target: list[int]) -> bool:
        heap = [-m for m in target]
        heapq.heapify(heap)
        while True:
            biggest = heapq.heappop(heap)
            rest = sum(heap)

            if -biggest == 1:
                return True

            if rest == 0 or biggest > rest:
                return False

            replaced = biggest % rest
            heapq.heappush(heap, replaced)

            if replaced > -1:
                return False


s = Solution()
target = [9, 3, 5]
# target = [1, 1000000000]
# target = [1, 1, 1, 2]

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
