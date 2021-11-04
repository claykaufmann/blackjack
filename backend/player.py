import json

# player class


class Player:

    def __init__(self, dealer: bool) -> None:
        # self.player = Player
        self.cards = []
        self.is_dealer = dealer
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
