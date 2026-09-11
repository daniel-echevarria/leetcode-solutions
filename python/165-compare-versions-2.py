class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")

        m, n = len(version1), len(version2)
        shortest = min(m, n)
        longest = max(m, n)

        for i in range(shortest):
            v1 = int(version1[i])
            v2 = int(version2[i])
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        survivor = version1 if len(version1) == longest else version2
        for i in range(shortest, longest):
            if int(survivor[i]) != 0:
                return 1 if survivor == version1 else -1
        return 0


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        m, n = len(version1), len(version2)

        for i in range(max(m, n)):
            n1 = int(version1[i]) if i < m else 0
            n2 = int(version2[i]) if i < n else 0

            if n1 < n2:
                return -1
            if n1 > n2:
                return 1
        return 0


# version1 = "7.5.2.4"
# version2 = "7.5.3"
version1 = "1"
version2 = "1.1"
s = Solution()
print(s.compareVersion(version1, version2))
