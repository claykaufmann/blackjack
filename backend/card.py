class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def to_string(self):
        return self.value + ' of ' + self.suit

    def json(self):
        """
        returns array of card info, index 0 being value, index 1 being suit
        """
        return [
            self.value,
            self.suit
        ]
