import json

# player class


class Player:

    def __init__(self, isDealer: bool) -> None:
        # self.player = Player
        self.cards = []
        self.is_dealer = isDealer
        self.value = 0

    def playerValue(cards):
        value = 0
        for card in cards:
            value = value + card.value
        return value

    def cards_as_json(self):
        return [card.json() for card in self.cards]
