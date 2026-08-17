class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = set()

        while l < r:
            r_changed = False
            for i in range(l + 1, r):
                curr_sum = nums[l] + nums[i] + nums[r]
                if curr_sum == 0:
                    res.add((nums[l], nums[i], nums[r]))
                elif curr_sum > 0:
                    r -= 1
                    r_changed = True
                    break
            if not r_changed:
                l += 1
        return list(res)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
        return list(res)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
        return res


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
        return res


# nums = [-1, 0, 1, 2, -1, -4]
# nums = [1, 2, 0, 1, 0, 0, 0, 0]
nums = [-100, -70, -60, 110, 120, 130, 160]
s = Solution()
print(s.threeSum(nums))
