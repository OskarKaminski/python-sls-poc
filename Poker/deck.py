import random

deck_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
deck_suits = ['h', 's', 'c', 'd']


class Deck:
    cards = []

    def __init__(self):
        self.cards = self.create_deck()

    def get_card(self):
        return self.cards.pop(random.randint(0, len(self.cards)))

    @staticmethod
    def create_deck():
        deck = []
        for value in deck_values:
            for suit in deck_suits:
                deck.append({
                    'value': value,
                    'suit': suit
                })
        return deck
