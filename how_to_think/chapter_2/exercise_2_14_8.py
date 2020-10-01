current_time = int(input("What is the current hour?"))
alarm_remaining = int(input("How long do you have to wait?"))
alarm_goes_off = (current_time + alarm_remaining) % 24

# using a 24 hour makes more sense to me, but I'm Dutch so maybe that is on me?
print("The alarm will go off at", alarm_goes_off)
