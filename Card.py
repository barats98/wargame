
class Card:
    VALUES = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
    SUITS = ('Diamond', 'Spade', 'Heart', 'Club')

    def __init__(self, value: int, suit: int):
        self.value: int = value
        self.suit: int = suit

    def  __lt__(self, other: 'Card'): #less than
        if self.value == 1:    #ace grater than other values
            if self.value < other.value:
                return False
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
        return False

    def __gt__(self, other):  #grater than
        return not self.__lt__(other)

    def __eq__(self, other: 'Card'):
        return self.value == other.value and self.suit == other.suit #equal

    def __str__(self): # convert to string
        return f"{Card.VALUES[self.value - 1]} {Card.SUITS[self.suit - 1]}" #fstring

    def __repr__(self): # presentation in print
        return f"{Card.VALUES[self.value - 1]} {Card.SUITS[self.suit - 1]}"






a = Card(10, 1)
b = Card(9, 3)

print(a < b)
