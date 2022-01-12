class Card:
    VALUES = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
    SUITS = ('Diamond', 'Spade', 'Heart', 'Club')

    def __init__(self, value: int, suit: int):
        if type(value) != int:
            raise TypeError("The value should be an int, honey!")
        if type(suit) != int:
            raise TypeError("The suit should be an int, honey!")
        if value <= 0 or value > 13:
            raise ValueError("The value should be between 1 and 13!")
        if suit <= 0 or suit > 4:
            raise ValueError("The suit should be between 1 and 4!")
        self.value: int = value
        self.suit: int = suit

    def __lt__(self, other: 'Card'):  # less than
        if self.value == 1:  # ace grater than other values
            if self.value < other.value:
                return False
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
        # if none of abobe returns was occured
        return False

    def __gt__(self, other):  #grater than
        return not self.__lt__(other)

    def __eq__(self, other: 'Card'):
        return self.value == other.value and self.suit == other.suit  # equal

    def __str__(self):  # convert to string
        return f"{Card.VALUES[self.value - 1]} {Card.SUITS[self.suit - 1]}"  # fstring

    def __repr__(self):  # presentation in print
        return f"{Card.VALUES[self.value - 1]} {Card.SUITS[self.suit - 1]}"
        # -1 because value in 1 ... 13 and VALUES indexec in 1 ... 12

if __name__ == '__main__':
    a = Card(1, 1)
    b = Card(1, 3)
    print(a < b)
    print(a > b)
    print(a)
    print(b)
