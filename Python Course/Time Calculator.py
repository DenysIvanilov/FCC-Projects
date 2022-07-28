def add_time(start, duration, day=False):

    def days_later():
        if days_passed == 0:
            return ""
        elif days_passed == 1:
            return " (next day)"
        else:
            return f" ({days_passed} days later)"

    day_map = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }

    week_days = {
        0: "monday",
        1: "tuesday",
        2: "wednesday",
        3: "thursday",
        4: "friday",
        5: "saturday",
        6: "sunday",
    }

    hrs, mins = start.split(":")
    mins, period = mins.split()
    dhrs, dmins = duration.split(":")
    hrs = int(hrs)
    mins = int(mins)
    dhrs = int(dhrs)
    dmins = int(dmins)

    thrs = hrs + dhrs
    tmins = mins + dmins
    if tmins >= 60:
        thrs += round(tmins // 60)
        tmins %= 60

    thr = thrs
    days_passed = 0
    if dhrs or dmins:
        while thr >= 24 or (thr >= 12 and period == "PM"):
            days_passed += 1
            thr -= 24
        thrr = thrs
        while True:
            if thrr < 12:
                break
            if thrr >= 12:
               if period == "AM":
                   period = "PM"
               elif period == "PM":
                   period = "AM"
            thrr -= 12

    hours = thrs % 12
    if hours == 0:
        hours = 12
    minutes = tmins
    dps = days_passed
    if day:
        if dps >= 7:
            dps %= 7
        day = day.strip().lower()
        starting_day = day_map[day]
        ending_day = week_days[(starting_day + dps) % 7]
        return f"{hours}:{minutes:02} {period}, {ending_day.capitalize()}{days_later()}"
    else:
        return f"{hours}:{minutes:02} {period}{days_later()}"

print(add_time("3:15 PM","424:35", "monday"))







