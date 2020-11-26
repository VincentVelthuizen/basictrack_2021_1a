class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "narf", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.ranks[self.rank], self.suits[self.suit])

    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1

        # Suits are the same, check the ranks
        if self.rank == other.rank:
            return 0
        if self.rank == 1 or (other.rank != 1 and self.rank > other.rank):
            return 1
        else:
            return -1

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0
