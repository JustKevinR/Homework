def hours_passed(time1, time2):

    if time1 == time2:
        return "no time passed"

    time1_clock, time1_period = time1.split()
    time2_clock, time2_period = time2.split()

    hrs1, minutes1 =  time1_clock.split(":")
    hrs2, minutes2 =  time2_clock.split(":")

    if time1_period == time2_period:
        return str(int(hrs2) - int(hrs1)) + " hours"
    else:
        return str(12 - int(hrs1)  + int(hrs2)) + " hours"

print(hours_passed("2:00 PM", "4:00 PM"))
