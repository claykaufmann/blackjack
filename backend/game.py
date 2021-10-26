from deck import Deck

"""
Game class represents a game of blackjack
"""


class Game():
    def __init__(self, id) -> None:
        self.id = id
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
