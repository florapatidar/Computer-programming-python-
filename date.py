def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def total_days(date):
    d, m, y = date
    month_days = [31, 28, 31, 30, 31, 30, 
                  31, 31, 30, 31, 30, 31]
    days = y * 365
    days += y // 4 - y // 100 + y // 400
    for i in range(m - 1):
        days += month_days[i]
    if m > 2 and is_leap(y):
        days += 1
    days += d
    
    return days
date1 = (10, 2, 2020)
date2 = (25, 3, 2023)
days_between = abs(total_days(date2) - total_days(date1))

print("Number of days between dates:", days_between)
