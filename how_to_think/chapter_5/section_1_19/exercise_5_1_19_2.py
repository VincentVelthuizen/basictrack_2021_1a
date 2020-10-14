# If you (like me) wondered what on earth this was in reference to: https://youtu.be/LBNjJmR5Yzw?t=249
# It is a children's tale about a family of ducks and these are the names of the ducklings.
prefixes = list("JKLMN")
prefixes.extend(["Ou", "P", "Qu"])

suffix = "ack"

for letter in prefixes:
    print(letter + suffix)
