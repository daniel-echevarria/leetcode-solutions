class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        start = list(start)
        result = list(result)
        a = b = 0

        while a < len(start):
            if start[a] == result[b]:
                a += 1
                b += 1
            elif start[b : b + 2] == ["X", "L"]:
                start[b : b + 2] = ["L", "X"]
            elif start[b : b + 2] == ["R", "X"]:
                start[b : b + 2] = ["X", "R"]
            else:
                return False
        return True


class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)
        start = list(start)
        result = list(result)
        a = b = 0

        while a < n:
            if result[b] == "L" and start[a] == "X":
                for i in range(b + 1, n):
                    if start[i] == "X":
                        continue
                    if start[i] == "L":
                        start[i], start[b] = start[b], start[i]
                        break
                    else:
                        return False

            elif result[b] == "X" and start[a] == "R":
                for i in range(b + 1, n):
                    if result[i] == "X":
                        continue
                    if result[i] == "R":
                        start[i], start[b] = start[b], start[i]
                        break
                    else:
                        return False
            if start[a] == result[b]:
                a += 1
                b += 1
            else:
                return False
        return True


class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if start.replace("X", "") != result.replace("X", ""):
            return False

        j = 0
        for i in range(len(start)):
            if start[i] == "L":
                while result[j] != "L":
                    j += 1
                if j > i:
                    return False
                j += 1
            if start[i] == "R":
                while result[j] != "R":
                    j += 1
                if i > j:
                    return False
                j += 1
        return True


# start = "X"
# result = "L"
start = "RXXLRXRXL"
result = "XRLXXRRLX"
# start = "RXXLRXRXL"
# result = "XRLXXRRLX"
# start = "XLXRRXXRXX"
# result = "LXXXXXXRRR"


# start = "LXXXXXRXXX"
# result = "LXXXXXXXRX"
s = Solution()
print(s.canTransform(start, result))
