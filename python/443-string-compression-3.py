class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        w = r = 0

        while r < n:
            char = chars[r]
            count = 0
            while r < n and chars[r] == char:
                count += 1
                r += 1
            num = count if count > 1 else ""
            s = f"{char}{num}"
            for l in s:
                chars[w] = l
                w += 1
        return w
