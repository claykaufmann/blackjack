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
        self.game_over = False

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
        # dealer action
        if self.dealer.value < 17:
            new_card = self.deck.deal()
            self.dealer.add_card(new_card)

        if action == "hit":
            new_card = self.deck.deal()
            self.player.add_card(new_card)
        elif action == "stay":
            return self.get_winner()
        else:
            return "error occurred"

        # check game conditions
        game_status = self.check_game_over()
        if game_status == True:
            return self.get_winner()

        # if we haven't returned, game is not over, continue game flow
        return False

    def check_game_over(self) -> bool:
        # check if player over 21
        if self.dealer.value > 21 and self.player.value > 21:
            return "tie"

        else:
            return False

    def get_winner(self) -> str:
        """This function returns the winner of the game"""
        self.game_over = True
