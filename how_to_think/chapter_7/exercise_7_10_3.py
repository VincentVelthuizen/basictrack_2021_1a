lines = ""
with open("snakes.txt") as snake_poem:
    lines = snake_poem.readlines()

with open("numbered_snakes.txt", "w") as numbered_snake_poem:
    for line_number, line in enumerate(lines):
        numbered_snake_poem.write(str(line_number + 1) + ": " + line)
