from Card import Card
from Deck import DeckOfCards

class Player:
    def __init__(self, name, number_of_cards=26):
        self.name = name
        self.number_of_cards = number_of_cards
        self.hand: [Card] = []

    def set_hand(self, deck: DeckOfCards):
        for i in range(self.number_of_cards):
            self.hand.append(deck.deal_one())

    def add_card(self, card):
        self.hand.append(card)





