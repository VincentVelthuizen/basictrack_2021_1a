from how_to_think.chapter_11.section_4_10.Card import Card
from how_to_think.chapter_11.section_5_9.CardGame import CardGame
from how_to_think.chapter_11.section_5_9.OldMaidHand import OldMaidHand


class OldMaidGame(CardGame):

    def __init__(self):
        super().__init__()
        self.hands = []

    def play(self, names):
        # Remove Queen of Clubs
        self.deck.remove(Card(0, 12))

        # Make a hand for each player
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print("{:-^30}".format("Cards have been dealt"))
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print("{:-^30}".format("Matches discarded, play begins"))
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("{:-^30}".format("Game is over"))
        self.print_hands()

    def print_hands(self):
        for hand in self.hands:
            print(hand)

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand {} picked {}".format(self.hands[i].name, picked_card))
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next_neighbor in range(1, num_hands):
            neighbor = (i + next_neighbor) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor
