class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        tickets_to_buy = tickets[k]
        time = 0
        for i in range(k + 1):
            time += min(tickets[i], tickets_to_buy)
        for i in range(k + 1, len(tickets)):
            time += min(tickets[i], tickets_to_buy - 1)
        return time


# Algo Bruteforce:
# while the person at index k has tickets to buy, keep going
# while the value at k index is bigger than 0
# iterate over the array and if the value is not 0
# add one second to the counter and the value gets -1

# Optimized:
# if the person has just one ticket, return k + 1
# otherwise iterate once over the array
# adding the min between the value and the number of tickets from
# the kth person

# tickets = [2, 3, 2]
# k = 2
tickets = [5, 1, 1, 1]
k = 0
# tickets = [84, 49, 5, 24, 70, 77, 87, 8]
# tickets = [5, 2, 3, 1]
# k = 3
s = Solution()
print(s.timeRequiredToBuy(tickets, k))
