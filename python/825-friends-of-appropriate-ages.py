class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        n = len(ages)
        i = 0
        while i < n and ages[i] < 15:
            i += 1

        ages = ages[i:]
        m = len(ages)
        j = 0
        res = 0
        while j < m:
            curr = ages[j]
            count = 0
            while j < m and ages[j] == curr:
                count += 1
                j += 1
            res += count * (count - 1)
            res += count * (j - count)
        return res


from collections import Counter


class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        counts = Counter(ages)
        ages.sort()

        j = 0
        k = 0
        res = 0
        for i, val in enumerate(ages):
            if ages[i] < 15:
                continue
            min_age = val * 0.5 + 7
            while ages[j] <= min_age:
                j += 1
            res += counts[ages[i]] - 1
            if ages[i] != ages[k]:
                k = i
            res += k - j
        return res


class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        counts = [0] * 121

        for age in ages:
            counts[age] += 1

        res = 0
        for a in range(15, 121):
            if counts[a] == 0:
                continue

            for b in range(15, 121):
                if counts[b] == 0:
                    continue

                if b <= a * 0.5 + 7:
                    continue
                if b > a:
                    continue

                res += counts[a] * (counts[b] - (a == b))
        return res


# ages = [4, 10, 15, 16, 16, 20, 30, 100, 110, 120]
ages = [20, 30, 100, 110, 120]
# ages = [16, 16]
s = Solution()
print(s.numFriendRequests(ages))
