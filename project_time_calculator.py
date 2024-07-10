def add_time(start, duration, day = None):
  # get start hour and minute
  start_hour = 0
  start_minute = 0
  start_time = start.split(':')
  for index, digit in enumerate(start_time):
    if index == 0:
      start_hour = int(digit)
    else:
      start_minute = int(digit[0:2])
  # convert time to 24-hour format
  if start[-2:].lower() == "pm":
    start_hour += 12

  # get duration hour and minute
  add_hour = 0
  add_minute = 0
  add_time = duration.split(':')
  for index, digit in enumerate(add_time):
    if index == 0:
      add_hour = int(digit)
    else:
      add_minute = int(digit[0:2])

  # get start day


  # calculate new time
  new_hour = start_hour + add_hour + ((start_minute + add_minute) // 60)
  new_minute = (start_minute + add_minute) % 60

  # convert to AM/PM format
  time_period = ""
  extra_day = 0
  if new_hour < 12:
    time_period = "AM"
  elif new_hour == 12:
    time_period = "PM"
  elif new_hour < 25:
    new_hour = new_hour % 12
    time_period = "PM"
  else:
    extra_day = new_hour // 24
    new_hour = new_hour % 24
    if new_hour == 0:
      new_hour = 12
      time_period = "AM"
    elif new_hour < 12:
      time_period = "AM"
    elif new_hour == 12:
      time_period = "PM"
    elif new_hour < 25:
      new_hour = new_hour % 12
      time_period = "PM"

  new_time = str(new_hour) + ':' + str(new_minute).rjust(2, '0') + ' ' + time_period

  if day is not None:
    start_day = get_start_day(day)
    end_day = get_end_day(start_day, extra_day)
    if extra_day == 0:
      new_time += f", {day}"
    elif extra_day == 1:
      new_time += f", {end_day} (next day)"
    else:
      new_time += f", {end_day} ({extra_day} days later)"
  else:
    if extra_day > 0 and extra_day < 2:
      new_time += f" (next day)"
    elif extra_day > 1:
      new_time += f" ({extra_day} days later)"

  print(new_time)
  return new_time

def get_start_day(day):
  if day.lower() == "monday":
    return 1
  elif day.lower() == "tuesday":
    return 2
  elif day.lower() == "wednesday":
    return 3
  elif day.lower() == "thursday":
    return 4
  elif day.lower() == "friday":
    return 5
  elif day.lower() == "saturday":
    return 6
  elif day.lower() == "sunday":
    return 7
  else:
    return 0

def get_end_day(start, duration):
  day = (start + duration) % 7
  if day == 0:
    return "Sunday"
  elif day == 1:
    return "Monday"
  elif day == 2:
    return "Tuesday"
  elif day == 3:
    return "Wedday"
  elif day == 4:
    return "Thursday"
  elif day == 5:
    return "Friday"
  elif day == 6:
    return "Saturday"
  else:
    return "N/A"


add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)


"""
Build a Time Calculator Project
Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

Example Code
add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

Note: open the browser console with F12 to see a more verbose output of the tests.
"""