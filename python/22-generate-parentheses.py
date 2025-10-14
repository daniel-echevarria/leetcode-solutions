class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        results = []
        def backtrack(path, moves):
