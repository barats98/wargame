import random
from random import shuffle
from Card import Card


class DeckMock:
    def __init__(self):
        self.current_card_in_deck = 52

    def cards_shuffle(self):
        pass

    def deal_one(self):
        self.current_card_in_deck -= 1
        return Card(10, 2)
