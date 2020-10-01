openings = ["Hi", "Hello", "Welcome", "Greetings", "Salutations", "Wazza"]

no_words_len_5 = 0
for word in openings:
    if len(word) == 5:
        no_words_len_5 += 1

print("There are", no_words_len_5, "words of length 5 in the list")
