with open("snakes.txt") as snake_poem:
    lines = snake_poem.readlines()

    for line in lines:
        if line.find("snake") >= 0:
            print(line)
