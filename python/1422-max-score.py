class Solution:
    def maxScore(self, s: str) -> int:
        left_score = 0
        right_score = s.count("1")
        max_score = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                left_score += 1
            else:
                right_score -= 1

            max_score = max(max_score, left_score + right_score)

        return max_score


s = Solution()
# st = "011101"
# st = "00111"
st = "1111"
# st = "00"
print(s.maxScore(st))


# Algo
# define a variable max_score and a current_score equal to 0
# Get the count of 0s and ones using count and subtracting that count from the length of s
# At the initial position the split pointer is at index 1
# the left_score is 1 or 0 depending on wether the first char is a 0 or a 1
# the right score is the 1's count minus the first character
# we iterate through the string and at each round
# if the char is a 0 with add 1 to left score
# if the char is a 1 we subtract 1 from right score
# we compare the current_total to the max score and update max_score if necessary
