current_time = 2 + 12 # plus 12 because pm
alarm_remaining = 51
alarm_goes_off = (current_time + alarm_remaining) % 24
print("The alarm will go off at", alarm_goes_off)
