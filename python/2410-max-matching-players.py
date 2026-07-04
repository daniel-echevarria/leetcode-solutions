class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        matches = p = t = 0

        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                matches += 1
                p += 1
                t += 1
            else:
                t += 1

        return matches


# Algo
# sort players and trainers
# loop while the indexes are smaller than their respective lists
# if the the trainer is bigger than the player, move both and add one to the counter
# otherwise just move the trainer
# return total
