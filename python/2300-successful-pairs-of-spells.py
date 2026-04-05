class Solution:
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:

        res = []
        potions.sort()
        m = len(potions)

        for s in spells:
            break_even = success / s
            l, r = 0, m - 1
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] < break_even:
                    l = mid + 1
                else:
                    r = mid - 1
            res.append(m - l)
        return res


spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7

s = Solution()
print(s.successfulPairs(spells, potions, success))


# Algo,sort potions
# for each spell, divide success by the spell's strength
# then find the first index in potions that is bigger or equal to that result
# append to the result array the total len of potions - that index
