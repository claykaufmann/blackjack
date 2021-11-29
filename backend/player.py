import json

from card import Card

# player class


class Player:

    def __init__(self, dealer: bool) -> None:
        # self.player = Player
        self.cards = []
        self.is_dealer = dealer
        self.value = 0

    def add_card(self, card: Card):
        # TODO: this card visibility is incorrect, dealers third card is visible
        if self.is_dealer == True and len(self.cards) > 2:
            card.change_visiblity(False)

        self.cards.append(card)
        if (card.value == "Ace"):
            self.value += 11
        else:
            self.value += card.value

    def cards_as_json(self):
        # handle change in react
        return [card.json() for card in self.cards]

    def set_card_visiblity(self):
        """
        this function sets the dealers first card to be visible, and all cards insvisible
        """
        if self.is_dealer == True:
            self.cards[len(self.cards) - 1].change_visiblity(False)

