deck_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Hand:

    def __init__(self) -> None:
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # Card is passed in from Deck.deal() method
        self.cards.append(card)
        self.value += deck_values[card.rank]

        # Track Aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # 0 is treated as FALSE when self.aces = 0
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1