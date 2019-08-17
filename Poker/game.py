from deck import Deck


class Game:

    def __init__(self):
        self.deck = Deck()
        self.players = []

    def add_player(self, name):
        self.players.append({
            'name': name
        })

    def start(self):
        for player in self.players:
            player.update({'cards': self.get_player_cards()})

    def get_player_cards(self):
        return [self.deck.get_card(), self.deck.get_card()]

