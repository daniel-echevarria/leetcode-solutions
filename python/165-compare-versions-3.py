class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        n, m = len(v1), len(v2)

        i = j = 0

        while i < n and j < m:
            if int(v1[i]) < int(v2[j]):
                return -1
            elif int(v1[i]) > int(v2[j]):
                return 1
            i += 1
            j += 1

        if i == n and m == n:
            return 0
        if i == n:
            return 0 if int("".join(v2[j:])) == 0 else -1
        return 0 if int("".join(v1[i:])) == 0 else 1


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        n, m = len(v1), len(v2)

        while n < m:
            v1.append("0")
            n += 1
        while m < n:
            v2.append("0")
            m += 1

        for i in range(n):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1

        return 0
