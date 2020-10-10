compass_points = ["N", "E", "S", "W"]


def turn_clockwise(start_direction):
    if start_direction not in compass_points:
        return None
    else:
        start_index = compass_points.index(start_direction)
        return compass_points[(start_index + 1) % len(compass_points)]


# Tests
print(turn_clockwise("N") == "E")
print(turn_clockwise("W") == "N")
