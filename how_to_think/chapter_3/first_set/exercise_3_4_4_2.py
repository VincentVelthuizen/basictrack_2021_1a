week_days = ["Sunday", "Monday", "Tuesday", "Wednesdau", "Thursday", "Friday", "Saturday"]

today = 3       # int(input("What is the start day? (0-6) "))
sleeps = 137    # int(input("How many sleeps?")

print("You will return on", week_days[(today + sleeps) % len(week_days)])
