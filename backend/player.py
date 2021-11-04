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

    def cards_as_json(self):
        # HACK: this needs to be changed to card.json() instead of card.value
        # handle change in react
        return [card.value for card in self.cards]
