from deck import Deck

"""
Game class represents a game of blackjack
"""


class Game():
    def __init__(self, id) -> None:
        self.id = id
        # TODO have player classes instantiate correctly
        self.player = Player(dealer=False)
        self.dealer = Player(dealer=True)
        self.deck = Deck()

    def initial_deal(self):
        player_card1 = self.deck.deal()
        player_card2 = self.deck.deal()

        dealer_card1 = self.deck.deal()
        dealer_card2 = self.deck.deal()

        # TODO update this to correctly add cards when methods are implemented
        self.player.add_card(player_card1)
        self.player.add_card(player_card2)

        self.dealer.add_card(player_card1)
        self.dealer.add_card(player_card2)

    # TODO impement this method...
    def action_input(self, action):
        if action == "hit":
            new_card = self.deck.deal()
            self.player.add_card(new_card)

        # dealer actions here
        if self.dealer.value < 17:
            new_card = self.deck.deal()
            self.dealer.add_card(new_card)

        # check game conditions
        game_status = check_end()

        # check if player went over 21...
        self.dealer.game_action()

        # check if dealer is over 21...

        # return game result

    def check_end(self):
        # check if player over 21

        #
