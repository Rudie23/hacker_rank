"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example:
    >>> s = '12:01:00PM'
    >>> conversion(s)
    '12:01:00'
    >>> s = '12:01:00AM'
    >>> conversion(s)
    '00:01:00'
"""


def conversion(time: str) -> str:
    hour_string = time[:2]
    minutes_string = time[2:]
    hour_number = int(hour_string)
    if time[-2:] == "AM":
        if hour_number >= 12:
            hour_string = "00"
            time_final = hour_string + minutes_string
            time_am = time_final[:-2]
        else:
            time_am = time[:-2]
        return time_am

    elif time[-2:] == "PM":
        if 12 > hour_number > 0:
            hour_number = hour_number + 12
            hour_string = str(hour_number)
            time_final = hour_string + minutes_string
            time_pm = time_final[:-2]
        else:
            time_pm = time[:-2]
        return time_pm


print(conversion('12:45:00PM'))
