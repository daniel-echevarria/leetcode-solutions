from collections import deque


class Solution:
    def isValidMutation(self, gene, mutation):
        result = []
        for i in range(len(gene)):
            if gene[i] == mutation[i]:
                continue
            result.append("mutation")
        return len(result) == 1

    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        visited = set([startGene])
        queue = deque([startGene])
        minMutations = 0
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                for mutation in bank:
                    if mutation in visited:
                        continue
                    if mutation == endGene and self.isValidMutation(current, mutation):
                        return minMutations + 1
                    if self.isValidMutation(current, mutation):
                        queue.append(mutation)
                        visited.add(mutation)
            minMutations += 1
        return -1


startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

s = Solution()
res = s.minMutation(startGene, endGene, bank)
# res = s.isValidMutation(startGene, bank[2])
print(res)
