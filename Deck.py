import random
from random import shuffle
from Card import Card


class DeckOfCards:
    def __init__(self):
        self.cards = [
            Card(value, suit)
            for value in range(1, len(Card.VALUES) + 1)
            for suit in range(1, len(Card.SUITS) + 1)
        ]  # LIST COMPREHENSION
        self.cards_shuffle()

    def cards_shuffle(self):
        shuffle(self.cards)

    def deal_one(self):
        card = random.choice(self.cards)  # возвращает случайный элемет последовательности
        self.cards.remove(card)  # remove the card
        return card
        # index = random.randint(0, len(self.cards) - 1)
        # card = self.cards[index]
        # del self.cards[index]
        # return card

print("Deck_name: ",__name__)
if __name__ == '__main__':
    my_deck = DeckOfCards()

    print(my_deck.cards)
    print(len(my_deck.cards))

    firstcard = my_deck.deal_one()
    print(firstcard)
    print(len(my_deck.cards))
