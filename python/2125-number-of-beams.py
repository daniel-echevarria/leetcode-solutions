class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        previous_row = bank[0].count("1")
        total_beams = 0
        for i in range(1, len(bank)):
            beams = bank[i].count("1")
            if beams > 0:
                total_beams += beams * previous_row
                previous_row = beams
        return total_beams


bank = ["011001", "000000", "010100", "001000"]
Output: 8

s = Solution()
print(s.numberOfBeams(bank))
