# some modes of travel
from week_10.Settings import Settings

settings = Settings(settings_file="travel_times_settings.txt")

# if I want to add a mode of travel I can add it to the file,
# the defaults list here is not used after the file has been created
modes_of_travel = settings.get("travel_modes", "walking,biking,driving").split(",")

speeds_of_travel = {}

for mode in modes_of_travel:
    speeds_of_travel[mode] = (settings.get(mode + "_speed"),
                              settings.get(mode + "_get_going"),
                              settings.get(mode + "_park"))

# ask the user for a distance
distance = float(input("Please provide the distance you would like to travel "))

# calculate travel times for each mode of travel and show to the user
for mode in speeds_of_travel:
    speed, get_going, park = speeds_of_travel[mode]
    travel_time = distance / speed + get_going / 60 + park / 60
    print("{} will take {:.2f} hours to get there.".format(mode, travel_time))
