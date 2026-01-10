import bisect


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        answer = []
        prefix_sum = []
        cur = 0
        for x in nums:
            cur += x
            prefix_sum.append(cur)

        for q in queries:
            answer.append(bisect.bisect(prefix_sum, q))
        return answer


s = Solution()
nums = [4, 5, 2, 1]
queries = [3, 10, 21]
print(s.answerQueries(nums, queries))
