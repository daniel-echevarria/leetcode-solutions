import bisect


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        if len(arr) == k:
            return arr
        start = bisect.bisect(arr, x)
        l = start - 1
        r = start
        res = []
        while k:
            if l < 0:
                res = res + arr[r : r + k]
                break
            if r > len(arr) - 1:
                res = arr[l + 1 - k : l + 1] + res
                break

            if abs(x - arr[l]) <= abs(x - arr[r]):
                res.append(arr[l])
                l -= 1
                k -= 1
            else:
                res.append(arr[r])
                r += 1
                k -= 1
        res.sort()
        return res


# arr = [1, 2, 3, 4, 5]
# k = 4
# x = 3
arr = [0, 1, 2, 2, 2, 3, 6, 8, 8, 9]
k = 5
x = 9
s = Solution()
print(s.findClosestElements(arr, k, x))
