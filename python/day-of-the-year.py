MONTH_DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))
        num_of_day = day
        if 2 < month and year % 4 == 0:
            num_of_day += 1
            if year % 10 == 0 and year % 400 != 0:
                num_of_day -= 1
        for i in range(month - 1):
            num_of_day += MONTH_DAYS[i]
        return num_of_day
