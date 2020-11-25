from how_to_think.chapter_11.section_4_10.Card import Card
import random


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        rng = random.Random()
        rng.shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

    def __str__(self):
        s = ""

        for index, card in enumerate(self.cards):
            s = s + " " * index + str(card) + "\n"

        return s
