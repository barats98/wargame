from Card import Card
from Deck import DeckOfCards

class Player:
    def __init__(self, name, number_of_cards=26):
        if type(name) != str:
            raise TypeError("The name should be a string, honey!")
        if type(number_of_cards) != int:
            raise TypeError("The number of cards should be an int")
        if number_of_cards <= 0:
            raise ValueError("Number of cards shoud be positive")
        self.name = name

        self.number_of_cards = number_of_cards
        self.hand: [Card] = []

    def set_hand(self, deck: DeckOfCards):
        for i in range(self.number_of_cards):
            self.hand.append(deck.deal_one())

    def add_card(self, card):
        self.hand.append(card)





if __name__ == "__main__":
    misha = Player("Misha", -1)