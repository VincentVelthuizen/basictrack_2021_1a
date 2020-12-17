import random


def show_card(card, size):
    longest_term = max([len(term) for term in terms])

    term_format = "{:^" + str(longest_term) + "}"
    line_format = term_format * size + "\n"
    card_format = line_format * size

    print(card_format.format(*card))


def mark_card_term(card):
    term_to_mark = input("Which term was called out?")
    if term_to_mark in card:
        card[card.index(term_to_mark)] = "X"
    else:
        print("that term wasn't on the card")


def mark_card_coordinate(card, size):
    column = int(input("Which column do you want to put the mark in? (start at 0)"))
    if column < 0 or column >= size:
        print("Invalid column number")
        return

    row = int(input("Which row do you want to put the mark in? (start at 0)"))
    if row < 0 or row >= size:
        print("Invalid row number")
        return

    index = (row * size) + column
    print("Marking", card[index])
    card[index] = "X"


def has_bingo(card, size):
    if card.count("X") < size: # Too few marks, no need to check the entire thing
        return False

    # rows
    for row in range(size):
        row_terms = card[(row * size):(row * size) + size]
        if size == row_terms.count("X"):
            return True

    # columns
    for column in range(size):
        column_terms = card[column::size]
        if size == column_terms.count("X"):
            return True

    # diagonals
    left_right_terms = card[::(size + 1)]
    if size == left_right_terms.count("X"):
        return True

    right_left_terms = card[(size - 1):(size + 1) * (size - 1):(size - 1)]
    if size == right_left_terms.count("X"):
        return True

    return False


with open("terms.txt", "r") as terms_file:
    terms = terms_file.read().splitlines()

card_size = int(input("how big should the card be? (standard card = 5)"))

random.shuffle(terms)                           # randomizes the list
unmarked_bingo_card = terms[:card_size ** 2]    # select the first card_size^2 terms from the randomized list
bingo_card = unmarked_bingo_card.copy()         # copy to mess with

while not has_bingo(bingo_card, card_size):
    show_card(bingo_card, card_size)
    mark_card_term(bingo_card)
    # mark_card_coordinate(bingo_card, card_size)

show_card(unmarked_bingo_card, card_size)
show_card(bingo_card, card_size)
print("You've got bingo!")
