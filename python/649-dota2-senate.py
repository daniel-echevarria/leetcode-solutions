from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = deque(senate)
        banning = deque()
        while senate:
            current = senate.popleft()
            if not banning or banning[0] == current:
                banning.append(current)
                continue
            senate.append(banning.popleft())
        return "Dire" if banning[0] == "D" else "Radiant"


senate = "DDRRR"
s = Solution()
print(s.predictPartyVictory(senate))
# iterate through the senate
# keep track of a banning list
# if the front of the queue is not the same
# move one of the banning to the end of the queue
# remove the front from the queue
# if at some point the all senate is the same
# declare victory for that senate
