class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:

        def invert(val):
            return 1 if val == 0 else 0

        n = len(image)
        for row in image:
            j, k = 0, n - 1
            while j < k:
                row[j], row[k] = row[k], row[j]
                row[j] = invert(row[j])
                row[k] = invert(row[k])
                j += 1
                k -= 1
        return image


class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        def invert(val):
            return 1 if val == 0 else 0

        return [[invert(x) for x in reversed(row)] for row in image]


image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
s = Solution()
print(s.flipAndInvertImage(image))
