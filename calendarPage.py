import calendar
import time

thisYear = int(time.strftime("%Y"))
thisMonth = int(time.strftime("%m"))


def generateCalendar(thisYear, thisMonth):
    prevMonth = thisMonth - 1
    nextMonth = thisMonth + 1
    if prevMonth == 0:
        prevMonth == 12
        prevYear = thisYear - 1
    if nextMonth == 13:
        nextMonth == 1
        nextYear = thisYear + 1
    cal = calendar.Calendar(firstweekday=0)
    currentMonthDays = list(cal.itermonthdays(thisYear, thisMonth))
    prevMonthDays = list(cal.itermonthdays(prevYear, prevMonth))
    nextMonthDays = list(cal.itermonthdays(nextYear, nextMonth))
    
    full_calendar = []

    

    

print(f"{thisYear}")
print(f"{thisMonth}")
# print(f"{prevMonth}")
# print(f"{nextMonth}")
