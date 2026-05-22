class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = []
        neg = []
        for n in nums:
            if n < 0:
                neg.append(n)
            else:
                pos.append(n)
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = 0
        neg = 0
        res = []
        next_is_pos = 1
        while len(res) < len(nums):
            if next_is_pos:
                while nums[pos] < 0:
                    pos += 1
                res.append(nums[pos])
                pos += 1
                next_is_pos = 0
            else:
                while nums[neg] > 0:
                    neg += 1
                res.append(nums[neg])
                neg += 1
                next_is_pos = 1
        return res


nums = [3, 1, -2, -5, 2, -4]
s = Solution()
print(s.rearrangeArray(nums))
