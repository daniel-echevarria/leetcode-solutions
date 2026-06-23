from collections import deque


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = deque(version1.split("."))
        version2 = deque(version2.split("."))

        while version1 or version2:
            v1 = int(version1.popleft()) if version1 else 0
            v2 = int(version2.popleft()) if version2 else 0
            if v1 > v2:
                return 1
            if v2 > v1:
                return -1
        return 0


version1 = "1.01"
version2 = "1.001"
# version1 = "1.2"
# version2 = "1.10"
s = Solution()
print(s.compareVersion(version1, version2))
