class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        is_interleave = False
        memo = set()

        def helper(cs1, cs2, cs3):
            nonlocal is_interleave

            if is_interleave:
                return

            state = (len(cs1), len(cs2))
            if state in memo:
                return

            if not cs1 and not cs2 and not cs3:
                is_interleave = True
                return

            if not cs3:
                memo.add(state)
                return

            if cs1:
                if cs1[0] == cs3[0]:
                    helper(cs1[1:], cs2, cs3[1:])
            if cs2:
                if cs2[0] == cs3[0]:
                    helper(cs1, cs2[1:], cs3[1:])
            memo.add(state)

        helper(s1, s2, s3)
        print(memo)
        return is_interleave


s = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(s.isInterleave(s1, s2, s3))


# Algo
# define a helper that given 3 strings tries all possibles paths to check if
# the 3rd one is an interleave of the first two
# it does so by exploring all possible paths and if it reaches a state
# where all strings are empty it changes the main isInterleave to true
# if all paths have been explored and this did ont happened return false
