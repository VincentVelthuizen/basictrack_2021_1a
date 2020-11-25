from how_to_think.chapter_11.section_4_10.Deck import Deck


class CardGame:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
