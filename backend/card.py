class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def to_string(self):
        return self.value + ' of ' + self.suit
