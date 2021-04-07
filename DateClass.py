# number of days in Jan, Feb, ..., Dec
MONTH_DAYS = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

def is_leap(year: int) -> int:
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return 366
    return 365

class Date():

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


    def convert_to_days(self):
        output = 0
        years = self.year - 1900
        for i in range(years):
            output += is_leap(1900 + i)
        output += self.day
        for i in range(self.month - 1):
            if i == 1 and is_leap(self.year == 366):
                output += 29
            else:
                output += MONTH_DAYS[i]
        return output


    def __sub__(self, other):
        return self.convert_to_days() - other.convert_to_days()


    def day_of_week(self):
        return (self.convert_to_days() % 7) - 1
