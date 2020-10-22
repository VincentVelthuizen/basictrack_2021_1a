# some modes of travel
modes_of_travel = ["walking", "biking", "driving"]

speeds_of_travel = {}

# check a file for information about those modes of travel
with open("travel_time.txt") as travel_time_file:
    for line in travel_time_file:
        mode, speed, get_going, park = line.split(",")
        speeds_of_travel[mode] = (float(speed), float(get_going), float(park))

# supplement that information if needed
for mode in modes_of_travel:
    if mode not in speeds_of_travel:
        speed = float(input("Please provide the speed of travel for " + mode + " "))
        get_going = float(input("Please provide the needed to get going with " + mode + " "))
        park = float(input("Please provide the time needed to park when " + mode + " "))
        speeds_of_travel[mode] = (speed, get_going, park)

# save the supplemented date to a file
with open("travel_time.txt", "w") as travel_time_file:
    for mode in speeds_of_travel:
        speed, get_going, park = speeds_of_travel[mode]
        travel_time_file.write(mode + "," + str(speed) + "," + str(get_going) + "," + str(park) + "")

# ask the user for a distance
distance = float(input("Please provide the distance you would like to travel "))

# calculate travel times for each mode of travel end show to the user
for mode in speeds_of_travel:
    speed, get_going, park = speeds_of_travel[mode]
    travel_time = distance / speed + get_going / 60 + park / 60
    print("{} will take {:.2f} hours to get there.".format(mode, travel_time))
