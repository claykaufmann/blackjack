class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def to_string(self):
        s = str(self.value) + " of " + self.suit
        return s

    def json(self):
        return {
            "value": self.value,
            "suit": self.suit
        }
