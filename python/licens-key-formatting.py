class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        full_plate = s.replace("-", "").upper()
        answer = []
        for i in range(len(full_plate), 0, -k):
            answer.append(full_plate[max(0, i - k) : i])
        return "-".join(reversed(answer))


s = Solution()
# st = "5F3Z-2e-9-w"
st = "2-5g-3-J"
k = 2
print(s.licenseKeyFormatting(st, k))


# Bruteforce:
# split the string by the dashes, convert it to uppercase
# join the string
# slice it up from the end while pushing it to an array
# reverse the array and join with a dash
