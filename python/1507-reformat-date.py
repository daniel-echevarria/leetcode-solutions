from datetime import datetime


class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        day = day[:-2].zfill(2)
        month = str(datetime.strptime(month, "%b").month).zfill(2)
        return "-".join([year, month, day])


s = Solution()
print(s.reformatDate("20th Oct 2052"))
