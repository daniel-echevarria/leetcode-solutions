class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        res = []
        min_dif = float("inf")
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            pair = [arr[i - 1], arr[i]]
            if diff < min_dif:
                res = [pair]
                min_dif = diff
                continue
            if diff == min_dif:
                res.append(pair)

        return res


s = Solution()
nums = [4, 2, 1, 3]
print(s.minimumAbsDifference(nums))


# Algo
# sort the array
# iterate through the sorted array while keepin track of the smallest difference
# append to the result and clean if found a smaller difference
