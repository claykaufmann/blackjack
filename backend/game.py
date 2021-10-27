from deck import Deck

"""
Game class represents a game of blackjack
"""


class Game():
    def __init__(self, id) -> None:
        self.id = id
        self.player = Player()
        self.dealer = Player()
        self.deck = Deck()

    def initial_deal(self):
        player_card1 = self.deck.deal()
        player_card2 = self.deck.deal()

        dealer_card1 = self.deck.deal()
        dealer_card2 = self.deck.deal()

        self.player.cards = [player_card1, player_card2]
        self.dealer.cards = [dealer_card1, dealer_card2]

    def action_input(self, action):
        if action == "hit":
            new_card = self.deck.deal()
            self.player.cards.append(new_card)

        # check if player went over 21...

        # check if dealer is over 21...

        # return game result
