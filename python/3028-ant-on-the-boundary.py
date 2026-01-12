class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        curr = 0
        back_to_boundary = 0

        for n in nums:
            curr += n
            if curr == 0:
                back_to_boundary += 1
        return back_to_boundary


s = Solution()
nums = [2, 3, -5]
print(s.returnToBoundaryCount(nums))
