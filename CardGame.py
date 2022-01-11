import random
from Card import Card
from Player import Player
from Deck import DeckOfCards


class CardGame:
    number_of_rounds = 40

    def __init__(self, names_of_players: [str], number_of_cards=26):
        self.start_game = False
        self.players = [Player(name, number_of_cards) for name in names_of_players]
        self.new_game()
        for round in range(CardGame.number_of_rounds):
            print("Current round", round + 1)
            self.print_start()
            self.one_round()
            winner = self.get_winner()
            if winner is not None:
                print(f"Winner after {round + 1} round: {winner.name}")
            else:
                print("No winner")
    def new_game(self):
        if self.start_game:
            print("Error")
            return
        deck = DeckOfCards()
        for player in self.players:
            player.set_hand(deck)
        self.start_game = True

    def get_winner(self):
        winner = self.players[0]
        has_winner = True
        #Идея в том чтобы удалить нулевой элемент из списка и ходить по списку начиная с первого, т
        #т.к нулевой уже хранится в перенной winner
        for player in self.players[1:]:
            if len(winner.hand) < len(player.hand):
                winner = player
                has_winner = True
            elif len(winner.hand) == len(player.hand):
                has_winner = False
        if has_winner:
            return winner

    def print_start(self):
        for player in self.players:
            print(f"{player.name}: {player.hand}")

    def one_round(self):
        round_cards = []
        for player in self.players:
            card = random.choice(player.hand)
            round_cards.append(card)
            player.hand.remove(card)
        winner_index = round_cards.index(max(round_cards))
        self.players[winner_index].hand.extend(round_cards) #  self.players[winner_index].hand += round_cards
        i = 0
        while i < len(self.players):
            if len(self.players[i].hand) == 0:
                del self.players[i]
            else:
                i += 1

if __name__ == '__main__':
    game = CardGame(['Eugeny', "Ilya"], 26)
