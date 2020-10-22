import random
import time

with open("terms.txt", "r") as terms_file:
    terms = terms_file.read().splitlines()

random.shuffle(terms)       # randomizes the list

timeout = int(input("How many seconds between terms?"))

for term in terms:
    print("The next term is:", term)
    time.sleep(timeout)
