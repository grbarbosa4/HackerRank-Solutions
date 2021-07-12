import calendar
def is_leap(year):
    return calendar.isleap(year) #calendar.isleap returns True if the year is leap, otherwise it returns False
    
year = int(input())
print(is_leap(year))
