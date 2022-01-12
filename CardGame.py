import random
from Card import Card
from Player import Player
from Deck import DeckOfCards


class CardGame:
    number_of_rounds = 40

    def __init__(self, names_of_players: [str], cards_per_player=26):
        max_card_per_player = DeckOfCards.DECK_LENGHT // len(names_of_players)
        if cards_per_player > 26 or cards_per_player < 10:  # number of cards per player
            raise ValueError(f"Card per player must be between 10 and 26")
        if cards_per_player > max_card_per_player:
            raise ValueError(f"Card per player must be equal or lower than {max_card_per_player}")
        self.is_game_started = False
        self.__init_players(names_of_players, cards_per_player)
        self.new_game()

    def print_winner(self, round=None):
        winner = self.get_winner()
        if winner is not None:
            if round is not None:
                print(f"Winner after {round + 1} round: {winner.name}")
            else:
                print(f"Winner: {winner.name}")
        else:
            print("Draw")

    def play_rounds(self, number_of_rounds):
        for round in range(CardGame.number_of_rounds):
            print("Current round", round + 1)
            self.print_start()
            self.one_round()
            self.print_winner(round)

    def __init_players(self, names_of_players, cards_per_player):
        self.players = []
        for name in names_of_players:
            self.players.append(Player(name, cards_per_player))
        # self.players = [Player(name, cards_per_player) for name in names_of_players]

    def new_game(self):
        if self.is_game_started:
            print("Error")
            return
        deck = DeckOfCards()
        for player in self.players:
            player.set_hand(deck)
        self.is_game_started = True

    def get_winner(self):
        winner = self.players[0]
        has_winner = True
        # Идея в том чтобы удалить нулевой элемент из списка и ходить по списку начиная с первого, т
        # т.к нулевой уже хранится в перенной winner
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

    def __generate_round_cards(self):
        round_cards = []
        for player in self.players:
            index = random.randint(0, len(player.hand) - 1)  # takes a random card from the player
            card = player.hand[index]  # card = random.choice(player.hand)
            del player.hand[index]  # player.hand.remove(card)
            round_cards.append(card)
        return round_cards

    def __delete_losers(self):  # if the player has no card the programm deletes him from the game
        i = 0
        while i < len(self.players):
            if len(self.players[i].hand) == 0:
                del self.players[i]
            else:
                i += 1

    def one_round(self):
        round_cards = self.__generate_round_cards()  #
        print(f"Cards in round: {round_cards}")
        winner_index = round_cards.index(max(round_cards))  # index of card with max value and index of winner player
        # we give cards to winner
        self.players[winner_index].hand.extend(round_cards)  # self.players[winner_index].hand += round_cards
        self.__delete_losers()


if __name__ == '__main__':
    game = CardGame(['Eugeny', "Ilya"], 26)
    game.play_rounds(10)
    game.print_winner()
