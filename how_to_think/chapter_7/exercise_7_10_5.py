# I don't think the dictionary they referred to actually is in the book anymore...
leet_speak = {  # search the internet for 1337 speak or leet speak for
    "l": "1",
    "e": "3",
    "t": "7",
    "a": "4",
    "o": "0"
}

lines = ""
# I feel somewhat ashamed for doing this to a poem
with open("snakes.txt") as snake_poem:
    for line in snake_poem:
        for letter in leet_speak:
            line = line.replace(letter, leet_speak[letter])
        print(line, end="")
