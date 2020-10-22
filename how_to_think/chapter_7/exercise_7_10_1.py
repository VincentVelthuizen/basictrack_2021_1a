lines = ""
with open("snakes.txt") as snake_poem:
    lines = snake_poem.readlines()

with open("reversed_snakes.txt", "w") as reversed_snake_poem:
    for line in reversed(lines):
        reversed_snake_poem.write(line)
