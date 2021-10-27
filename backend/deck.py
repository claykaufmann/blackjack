# deck class

import random
from card import Card

# list containing the suits
suitsList = ["Spades", "Clubs", "Diamonds", "Hearts"]

class Deck:

    # initializer
    def __init__(self):
        # empty array to hold cards
        self.cards = []
        self.buildDeck()

    # create a deck of cards using Card class
    def buildDeck(self):
        # iterate through suits and then values 1 - 14
        for s in suitsList:
            for i in range(2, 14):
                # anything 10 or higher is automatically a 10
                if i <= 9:
                    self.cards.append(Card(s, i))
                elif i == 11:
                    self.cards.append(Card("Ace", i))
                else:
                    self.cards.append(Card(s, 10))

    # randomly deal a single card
    def deal(self):
        # get a random card using a random index
        randIndex = random.randrange(len(self.cards))
        dealtCard = self.cards[randIndex]

        # remove that card from the deck
        self.cards.remove(dealtCard)

        # return (deal) the randomly selected card
        return dealtCard

