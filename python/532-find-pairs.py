class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        pairs = set()
        i = j = 0
        while j < n:
            if i == j or nums[j] - nums[i] < k:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
            else:
                pairs.add((nums[i], nums[j]))
                i += 1
                j += 1
        return len(pairs)


# nums = [3, 1, 4, 1, 5, -7]
# nums = [1, 3, 1, 5, 4]
# k = 0

nums = [1, 2, 4, 4, 3, 3, 0, 9, 2, 3]
k = 3
s = Solution()
print(s.findPairs(nums, k))
