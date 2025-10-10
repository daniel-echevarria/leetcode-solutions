class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        results = []
        stored = set()

        def helper(i):
            option = nums[:]
            for j in range(n):
                option[j] = nums[i]
                option[i] = nums[j]
                string_version = "".join(list(map(str, option)))
                if string_version not in stored:
                    results.append(option)
                stored.add(string_version)
                option = nums[:]

        for i in range(n):
            helper(i)
        print(results)
        return results


s = Solution()
s.permute([1, 2, 3])
