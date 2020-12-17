import random

with open("terms.txt", "r") as terms_file:
    terms = terms_file.read().splitlines()

random.shuffle(terms)       # randomizes the list

for term in terms:
    print("The next term is:", term)
    if input("next?") not in ["", "y", "yes"]:
        break
