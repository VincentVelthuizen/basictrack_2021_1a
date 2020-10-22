lines = ""
with open("numbered_snakes.txt") as snake_poem:
    lines = snake_poem.readlines()

with open("unnumbered_snakes.txt", "w") as unnumbered_snake_poem:
    for line_number, line in enumerate(lines):
        unnumbered_snake_poem.write(line.replace(str(line_number + 1) + ": ", ""))
