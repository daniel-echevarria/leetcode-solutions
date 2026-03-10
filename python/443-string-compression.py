class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        res = ""
        current = chars[0]
        count = 1
        for i in range(1, n):
            if chars[i] == current:
                count += 1
                continue
            else:
                if count < 2:
                    res += chars[i]
                else:
                    res += current + str(count)
                current = chars[i]
                count = 1
        if count < 2:
            res += current
        else:
            res += current + str(count)
        chars = list(res)
        print(res)
        return len(chars)


class Solution:
    def compress(self, chars: list[str]) -> int:
        s = []
        current = ""
        count = 0
        while chars:
            c = chars.pop()
            if c == current:
                count += 1
                continue
            if count > 1:
                s.append((str(count)))
            if current:
                s.append(current)
            current = c
            count = 1
        if count > 1:
            s.append(str(count))
        s.append(current)

        while s:
            chars.extend(list(s.pop()))
        print(chars)
        return len(chars)


class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        count = 0
        l = r = current = 0
        while r < n:
            if chars[current] == chars[r]:
                count += 1
                r += 1
                continue
            if count > 1:
                for c in str(count):
                    chars[l + 1] = c
                    l += 1

            current = r
            count = 0
        if count > 1:
            for c in str(count):
                chars[l + 1] = c
                l += 1
        l += 1
        return l + 1


class Solution:
    def compress(self, chars: list[str]) -> int:
        current = chars[0]
        count = 1
        w, r = -1, 1
        while r < len(chars):
            if chars[r] == current:
                count += 1
                r += 1
                continue
            w += 1
            chars[w] = current
            if count > 1:
                for n in str(count):
                    w += 1
                    chars[w] = n
            current = chars[r]
            count = 0
        w += 1
        chars[w] = current
        if count > 1:
            for n in str(count):
                w += 1
                chars[w] = n
        return w + 1


s = Solution()
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
# chars = ["a", "a", "a", "b", "b", "a", "a"]
print(s.compress(chars))

# Algo
# keep track of the result string
# and the current value
# iterate through the chars
# if the chars is the same than the current value add one to the count
# otherwise add the char + the count to the result string
# after iteration replace the first char with the compressed value
