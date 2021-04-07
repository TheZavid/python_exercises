class Time():
    def __init__(self, hours, minutes, am_pm):
        self.hours = hours
        self.minutes = minutes
        self.am_pm = am_pm.upper()


    def __repr__(self):
        return str(self.hours) + ":" + f'{self.minutes:02d}' + ' ' + self.am_pm


    def __add__(self, other):
        new_hours = self.hours % 12
        ap = self.am_pm
        if ap == 'PM':
            new_hours += 12
        total_min = new_hours * 60 + self.minutes + other
        new_hours = total_min // 60
        new_min = total_min % 60
        del total_min
        new_hours %= 24
        if new_hours >= 12:
            ap = 'PM'
        else:
            ap = 'AM'
        new_hours %= 12
        if new_hours == 0:
            new_hours = 12
        # ap = self.am_pm
        # new_min = self.minutes + other
        # new_hours = self.hours
        # while new_min < 0 :
        #     new_hours -= 1
        #     new_min += 60
        #     if new_hours == 11:
        #         if ap == 'AM':
        #             ap = 'PM'
        #         else:
        #             ap = "AM"
        #     if new_hours == 0:
        #         new_hours = 12
        # while new_min > 60:
        #     new_hours += 1
        #     new_min -= 60
        #     if new_hours == 12:
        #         if ap == 'AM':
        #             ap = 'PM'
        #         else:
        #             ap = "AM"
        #     if new_hours == 13:
        #         new_hours = 1
        return Time(new_hours, new_min, ap)

t = Time(7, 4, 'pm') # 7:04 PM
u = t + (5 * 60 + 2) # add 5 hours and 2 minutes
print(u) # prints '12:06 AM'
v = u + 70 # add 70 minutes
print(v) # prints '1:16 AM'
print(v +  (- 120)) # prints '11:16 PM'
