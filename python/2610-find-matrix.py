from collections import defaultdict


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        res = []
        counts = defaultdict(int)
        for n in nums:
            count = counts[n]
            if len(res) < count + 1:
                res.append([])
            res[count].append(n)
            counts[n] += 1
        return res


nums = [1, 3, 4, 1, 2, 3, 1]
s = Solution()
print(s.findMatrix(nums))


# iterate through nums while keeping count, for each num
# place it in the count array and add one to the count
# if the array does not exist, create it and place it there
