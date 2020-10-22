with open("terms.txt", "r") as terms_file:
    terms = terms_file.read().splitlines()

with open("terms.txt", "a+") as terms_file:
    new_term = input("Type a word to add it to the list or just hit enter to quit: ")

    while new_term != "":
        if new_term in terms:
            print(new_term, "was already in the list")
        else:
            terms.append(new_term)
            terms_file.write(new_term + "\n")
            print("The list now contains", len(terms))

        new_term = input("Type a word to add it to the list or just hit enter to quit: ")
