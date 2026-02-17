from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        l, r = 0, min(k, len(nums))
        while r <= len(nums):
            window = nums[l : r + 1]
            if len(window) > len(set(window)):
                return True
            l += 1
            r += 1
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        counts = defaultdict(int)
        l, r = 0, min(k, len(nums))
        for i in range(r + 1):
            counts[nums[i]] += 1
            if counts[nums[i]] > 1:
                return True
        for i in range(r, len(nums)):
            l += 1
            counts[nums[l]] -= 1
            counts[nums[i]] += 1
            if counts[nums[r]] > 1:
                return True
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        if k + 1 >= n:
            return n != len(set(nums))
        l, r = 0, k + 1
        count = defaultdict(int)
        for x in nums[:r]:
            count[x] += 1
            if count[x] > 1:
                return True
        while True:
            l += 1
            r += 1
            if r > n - 1:
                return False
            count[nums[l - 1]] -= 1
            if count[nums[l - 1]] < 0:
                count[nums[l - 1]] = 0
            count[nums[r]] += 1
            if count[nums[r]] > 1:
                return True


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        for i, n in enumerate(nums):
            if n in window:
                return True
            window.add(n)
            if len(window) > k:
                window.remove(nums[i - k])
        return False


s = Solution()
# nums = [1, 2, 3, 1]
# k = 3
# nums = [99, 99, 1, 3, 4]
# k = 3
# nums = [2, 2]
# k = 3
# nums = [1, 0, 1, 1]
# k = 1
# nums = [1, 2, 3, 1, 2, 1, 3]
# k = 1
print(s.containsNearbyDuplicate(nums, k))
