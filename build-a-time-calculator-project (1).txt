** start of main.py **

def add_time(start, duration, day_name=None):
    #list of days in the week
    day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # Separate hours and minutes of start time
    start_hour = int(start.split(':')[0])
    start_minute = int(start.split(':')[1].split()[0])
    am_pm = start.split()[1]

    # Covert PM to 24h format
    if am_pm == 'PM' and start_hour != 12:
        start_hour += 12
    elif am_pm == "AM" and start_hour ==12:
        start_hour = 0
    # Separate hours and minutes from duration
    add_hour = int(duration.split(':')[0])
    add_minute = int(duration.split(':')[1])

    #Add time
    total_minutes = start_hour * 60 + start_minute + add_hour * 60 + add_minute

    #caculate new day, hours and minutes:
    days = total_minutes // (24*60)
    new_total_minutes = total_minutes % (24 * 60)
    new_hour_24 = new_total_minutes // 60
    new_minute = new_total_minutes % 60

    #determine AM/ PM
    if new_hour_24 >= 12:
        am_pm = 'PM'
    else:
        am_pm = 'AM'
    #return 12h format:
    new_hour = new_hour_24 % 12
    if new_hour == 0:
        new_hour = 12
    #Process new day if day_name is present
    new_day_str = ""
    if day_name:
        day_name = day_name.capitalize()
        if day_name in day_list:
            new_day_index = (day_list.index(day_name) + days) % 7
            new_day_str = day_list[new_day_index]
    #Create a daily notification sequence
    if days== 0:
        day_later_str = ""
    elif days == 1:
        day_later_str = "(next day)"
    else:
        day_later_str = f"({days} days later)"

    #create a final result

    if day_name:
        final_result = f"{new_hour}:{new_minute:02} {am_pm}, {new_day_str} {day_later_str}".strip()
    else:
        final_result = f"{new_hour}:{new_minute:02} {am_pm} {day_later_str}".strip()
    return final_result


** end of main.py **

